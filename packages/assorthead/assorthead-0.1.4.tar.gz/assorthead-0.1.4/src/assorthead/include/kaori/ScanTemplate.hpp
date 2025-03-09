#ifndef KAORI_SCAN_TEMPLATE_HPP
#define KAORI_SCAN_TEMPLATE_HPP

#include <bitset>
#include <vector>
#include <stdexcept>
#include <string>

#include "utils.hpp"

/**
 * @file ScanTemplate.hpp
 *
 * @brief Defines the `ScanTemplate` class.
 */

namespace kaori {

/**
 * @brief Scan a read sequence for the template sequence.
 *
 * When searching for barcodes, **kaori** first searches for a "template sequence" in the read sequence.
 * The template sequence contains constant regions interspersed with one or more variable regions.
 * The template is realized into the full barcoding element by replacing each variable region with one sequence from the corresponding pool of barcodes.
 *
 * This class will scan read sequence to find a location that matches the constant regions of the template, give or take any number of substitutions.
 * Multiple locations on the read may match the template, provided `next()` is called repeatedly.
 * For efficiency, the search itself is done after converting all base sequences into a bit encoding.
 * The maximum size of this encoding is determined at compile-time by the `max_length` template parameter.
 *
 * Once a match is found, the sequence of the read at each variable region can be matched against a pool of known barcode sequences.
 * See the `BarcodePool` class for details.
 *
 * @tparam max_size Maximum length of the template sequence.
 */
template<size_t max_size>
class ScanTemplate { 
private:
    static constexpr size_t N = max_size * 4;

public:
    /**
     * Default constructor.
     * This is only provided to enable composition, the resulting object should not be used until it is copy-assigned to a properly constructed instance.
     */
    ScanTemplate() {}

    /**
     * @param[in] template_seq Pointer to a character array containing the template sequence.
     * Constant sequences should only contain `A`, `C`, `G` or `T` (or their lower-case equivalents).
     * Variable regions should be marked with `-`.
     * @param template_length Length of the array pointed to by `template_seq`.
     * This should be less than or equal to `max_size`.
     * @param strand Strand(s) of the read sequence to search.
     */
    ScanTemplate(const char* template_seq, size_t template_length, SearchStrand strand) :
        length(template_length), forward(search_forward(strand)), reverse(search_reverse(strand))
    {
        if (length > max_size) {
            throw std::runtime_error("maximum template size should be " + std::to_string(max_size) + " bp");
        }

        if (forward) {
            for (size_t i = 0; i < length; ++i) {
                char b = template_seq[i];
                if (b != '-') {
                    add_base_to_hash(forward_ref, b);
                    add_mask_to_hash(forward_mask);
                    forward_mask_ambiguous.set(i);
                } else {
                    shift_hash(forward_ref);
                    shift_hash(forward_mask);
                    add_variable_base(forward_variables, i);
                }
            }
        } else {
            // Forward variable regions are always defined.
            for (size_t i = 0; i < length; ++i) {
                char b = template_seq[i];
                if (b == '-') {
                    add_variable_base(forward_variables, i);
                }
            }
        }

        if (reverse) {
            for (size_t i = 0; i < length; ++i) {
                char b = template_seq[length - i - 1];
                if (b != '-') {
                    add_base_to_hash(reverse_ref, complement_base(b));
                    add_mask_to_hash(reverse_mask);
                    reverse_mask_ambiguous.set(i);
                } else {
                    shift_hash(reverse_ref);
                    shift_hash(reverse_mask);
                    add_variable_base(reverse_variables, i);
                }
            }
        }
    }

public:
    /**
     * @brief Details on the current match to the read sequence.
     */
    struct State {
        /**
         * Position of the match.
         * This should only be used once `next()` is called.
         */
        size_t position = static_cast<size_t>(-1); // overflow should be sane.

        /**
         * Number of mismatches on the forward strand.
         * This should only be used once `next()` is called.
         */
        int forward_mismatches = -1;

        /**
         * Number of mismatches on the reverse strand.
         * This should only be used once `next()` is called.
         */
        int reverse_mismatches = -1;

        /**
         * Whether the match is at the end of the read sequence.
         * If `true`, `next()` should not be called.
         */
        bool finished = false;

        /**
         * @cond
         */
        std::bitset<N> state;
        const char * seq;
        size_t len;

        std::bitset<N/4> ambiguous; // we only need a yes/no for the ambiguous state, so we can use a smaller bitset.
        size_t last_ambiguous; // contains the position of the most recent ambiguous base; should only be read if any_ambiguous = true.
        bool any_ambiguous = false; // indicates whether ambiguous.count() > 0.
        /**
         * @endcond
         */
    };

    /**
     * Begin a new search for the template in a read sequence.
     *
     * @param[in] read_seq Pointer to an array containing the read sequence.
     * @param read_length Length of the read sequence.
     *
     * @return An empty `State` object.
     * If its `finished` member is `false`, it should be passed to `next()` before accessing its other members.
     * If `true`, the read sequence was too short for any match to be found.
     */
    State initialize(const char* read_seq, size_t read_length) const {
        State out;
        out.seq = read_seq;
        out.len = read_length;

        if (length <= read_length) {
            for (size_t i = 0; i < length - 1; ++i) {
                char base = read_seq[i];

                if (is_standard_base(base)) {
                    add_base_to_hash(out.state, base);

                    if (out.any_ambiguous) {
                        out.ambiguous <<= 1;
                    }
                } else {
                    add_other_to_hash(out.state);

                    if (out.any_ambiguous) {
                        out.ambiguous <<= 1;
                    } else {
                        out.any_ambiguous = true;
                    }
                    out.ambiguous.set(0);
                    out.last_ambiguous = i;
                }
            }
        } else {
            out.finished = true;
        }

        return out;
    }

    /**
     * Find the next match in the read sequence.
     * The first invocation will search for a match at position 0;
     * this can be repeatedly called until `match.finished` is `true`.
     *
     * @param state A `State` object produced by `initialize()`.
     * On return, `state` is updated with the details of the current match at a particular position on the read sequence.
     */
    void next(State& state) const {
        size_t right = state.position + length;
        char base = state.seq[right];

        if (is_standard_base(base)) {
            add_base_to_hash(state.state, base); // no need to trim off the end, the mask will handle that.
            if (state.any_ambiguous) {
                state.ambiguous <<= 1;

                // If the last ambiguous position is equal to 'position', the
                // ensuing increment to the latter will shift it out of the
                // hash... at which point, we've got no ambiguity left.
                if (state.last_ambiguous == state.position) {
                    state.any_ambiguous = false;
                }
            }

        } else {
            add_other_to_hash(state.state);

            if (state.any_ambiguous) {
                state.ambiguous <<= 1;
            } else {
                state.any_ambiguous = true;
            }
            state.ambiguous.set(0);
            state.last_ambiguous = right;
        }

        ++state.position;
        full_match(state);
        if (right + 1 == state.len) {
            state.finished = true;
        }

        return;
    }

private:
    std::bitset<N> forward_ref, forward_mask;
    std::bitset<N> reverse_ref, reverse_mask;
    size_t length;
    int mismatches;
    bool forward, reverse;

    std::bitset<N/4> forward_mask_ambiguous; // we only need a yes/no for whether a position is an ambiguous base, so we can use a smaller bitset.
    std::bitset<N/4> reverse_mask_ambiguous;

    static void add_mask_to_hash(std::bitset<N>& current) {
        shift_hash(current);
        current.set(0);
        current.set(1);
        current.set(2);
        current.set(3);
        return;
    }

    static int strand_match(const State& match, const std::bitset<N>& ref, const std::bitset<N>& mask, const std::bitset<N/4>& mask_ambiguous) {
        // pop count here is equal to the number of non-ambiguous mismatches *
        // 2 + number of ambiguous mismatches * 3. This is because
        // non-ambiguous bases are encoded by 1 set bit per 4 bases (so 2 are
        // left after a XOR'd mismatch), while ambiguous mismatches are encoded
        // by all set bits per 4 bases (which means that 3 are left after XOR).
        size_t pcount = ((match.state & mask) ^ ref).count(); 

        if (match.any_ambiguous) {
            size_t acount = (match.ambiguous & mask_ambiguous).count();
            return (pcount - acount) / 2; // i.e., acount + (pcount - acount * 3) / 2;
        } else {
            return pcount / 2;
        }
    }

    void full_match(State& match) const {
        if (forward) {
            match.forward_mismatches = strand_match(match, forward_ref, forward_mask, forward_mask_ambiguous);
        }
        if (reverse) {
            match.reverse_mismatches = strand_match(match, reverse_ref, reverse_mask, reverse_mask_ambiguous);
        }
    }

private:
    std::vector<std::pair<int, int> > forward_variables, reverse_variables;

public:
    /**
     * Extract details about the variable regions in the template sequence.
     *
     * @tparam reverse Should we return the coordinates of the variable regions when searching on the reverse strand?
     *
     * @return A vector of pairs where each pair specifies the start and one-past-the-end position of each variable region in the template.
     * Coordinates are reported relative to the start of the template.
     * Pairs are ordered by the start positions.
     * If `reverse = true`, coordinates are reported after reverse-complementing the template sequence.
     */
    template<bool reverse = false>
    const std::vector<std::pair<int, int> >& variable_regions() const {
        if constexpr(reverse) { 
            return reverse_variables;
        } else {
            return forward_variables;
        }
    } 

private:
    static void add_variable_base(std::vector<std::pair<int, int> >& variables, int i) {
        if (!variables.empty()) {
            auto& last = variables.back().second;
            if (last == i) {
                ++last;
                return;
            }
        }
        variables.emplace_back(i, i + 1);
        return;
    }
};

}

#endif
