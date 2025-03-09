#ifndef KNNCOLLE_ANNOY_HPP
#define KNNCOLLE_ANNOY_HPP

#include <vector>
#include <type_traits>
#include <algorithm>
#include <memory>

#include "knncolle/knncolle.hpp"
#include "annoy/annoylib.h"
#include "annoy/kissrandom.h"

/**
 * @file knncolle_annoy.hpp
 * @brief Approximate nearest neighbor search with Annoy.
 */

/**
 * @namespace knncolle_annoy
 * @brief Approximate nearest neighbor search with Annoy.
 */
namespace knncolle_annoy {

/**
 * @brief Options for `AnnoyBuilder()` and `AnnoyPrebuilt()`.
 */
struct AnnoyOptions {
    /**
     * Number of trees to construct.
     * Larger values improve accuracy at the cost of index size (i.e., memory usage), see [here](https://github.com/spotify/annoy#tradeoffs) for details.
     */
    int num_trees = 50;

    /**
     * Factor that is multiplied by the number of neighbors `k` to determine the number of nodes to search in `find_nearest_neighbors()`.
     * Larger values improve accuracy at the cost of runtime, see [here](https://github.com/spotify/annoy#tradeoffs) for details.
     * If set to -1, it defaults to `num_trees`.
     */
    double search_mult = -1;
};

template<class Distance_, typename Dim_, typename Index_, typename Float_, typename InternalIndex_, typename InternalData_>
class AnnoyPrebuilt;

/**
 * @brief Searcher on an Annoy index.
 *
 * Instances of this class are usually constructed using `AnnoyPrebuilt::initialize()`.
 *
 * @tparam Distance_ An **Annoy** class to compute the distance between vectors, e.g., `Annoy::Euclidean`.
 * @tparam Dim_ Integer type for the number of dimensions.
 * @tparam Index_ Integer type for the indices.
 * @tparam Float_ Floating point type for the query data and output distances.
 * @tparam InternalIndex_ Integer type for the internal indices in Annoy.
 * @tparam InternalData_ Floating point type for the internal data in Annoy.
 */
template<class Distance_, typename Dim_, typename Index_, typename Float_, typename InternalIndex_, typename InternalData_>
class AnnoySearcher : public knncolle::Searcher<Index_, Float_> {
private:
    const AnnoyPrebuilt<Distance_, Dim_, Index_, Float_, InternalIndex_, InternalData_>* my_parent;

    static constexpr bool same_internal_data = std::is_same<Float_, InternalData_>::value;
    typename std::conditional<!same_internal_data, std::vector<InternalData_>, bool>::type my_buffer, my_distances;

    static constexpr bool same_internal_index = std::is_same<Index_, InternalIndex_>::value;
    std::vector<InternalIndex_> my_indices;

    int get_search_k(int k) const {
        if (my_parent->my_search_mult < 0) {
            return -1;
        } else {
            return my_parent->my_search_mult * static_cast<double>(k) + 0.5; // rounded.
        }
    }

public:
    /**
     * @cond
     */
    AnnoySearcher(const AnnoyPrebuilt<Distance_, Dim_, Index_, Float_, InternalIndex_, InternalData_>* parent) : my_parent(parent) {
        if constexpr(!same_internal_data) {
            my_buffer.resize(my_parent->my_dim);
        }
    }
    /**
     * @endcond
     */

private:
    auto obtain_pointers(std::vector<Index_>* output_indices, std::vector<Float_>* output_distances, Index_ k) {
        std::vector<InternalIndex_>* icopy_ptr = &my_indices;
        if (output_indices) {
            if constexpr(same_internal_index) {
                icopy_ptr = output_indices;
            }
        }
        icopy_ptr->clear();
        icopy_ptr->reserve(k);

        std::vector<InternalData_>* dcopy_ptr = NULL;
        if (output_distances) {
            if constexpr(same_internal_data) {
                dcopy_ptr = output_distances;
            } else {
                dcopy_ptr = &my_distances;
            }
            dcopy_ptr->clear();
            dcopy_ptr->reserve(k);
        }

        return std::make_pair(icopy_ptr, dcopy_ptr);
    }

    template<typename Type_>
    static void remove_self(std::vector<Type_>& vec, size_t at) {
        if (at < vec.size()) {
            vec.erase(vec.begin() + at);
        } else {
            vec.pop_back();
        }
    }

    template<typename Source_, typename Dest_>
    static void copy_skip_self(const std::vector<Source_>& source, std::vector<Dest_>& dest, size_t at) {
        auto sIt = source.begin();
        size_t end = source.size();
        dest.clear();
        dest.reserve(end - 1);

        if (at < end) {
            dest.insert(dest.end(), sIt, sIt + at);
            dest.insert(dest.end(), sIt + at + 1, source.end());
        } else {
            // Just in case we're full of ties at duplicate points, such that 'c'
            // is not in the set.  Note that, if self_found=false, we must have at
            // least 'k+2' points for 'c' to not be detected as its own neighbor.
            // Thus there is no need to worry whether 'end - 1 != k'; we
            // are guaranteed to return 'k' elements in this case.
            dest.insert(dest.end(), sIt, sIt + end - 1);
        }
    }

public:
    /**
     * @copydoc knncolle::Searcher::search() 
     */
    void search(Index_ i, Index_ k, std::vector<Index_>* output_indices, std::vector<Float_>* output_distances) {
        Index_ kp1 = k + 1; // +1, as it forgets to discard 'self'.
        auto ptrs = obtain_pointers(output_indices, output_distances, kp1);
        auto icopy_ptr = ptrs.first;
        auto dcopy_ptr = ptrs.second;

        my_parent->my_index.get_nns_by_item(i, kp1, get_search_k(kp1), icopy_ptr, dcopy_ptr);

        size_t at;
        {
            const auto& cur_i = *icopy_ptr;
            at = cur_i.size();
            InternalIndex_ icopy = i;
            for (size_t x = 0, end = cur_i.size(); x < end; ++x) {
                if (cur_i[x] == icopy) {
                    at = x;
                    break;
                }
            }
        }

        if (output_indices) {
            if constexpr(same_internal_index) {
                remove_self(*output_indices, at);
            } else {
                copy_skip_self(my_indices, *output_indices, at);
            }
        }

        if (output_distances) {
            if constexpr(same_internal_data) {
                remove_self(*output_distances, at);
            } else {
                copy_skip_self(my_distances, *output_distances, at);
            }
        }
    }

private:
    void search_raw(const InternalData_* query, Index_ k, std::vector<Index_>* output_indices, std::vector<Float_>* output_distances) {
        auto ptrs = obtain_pointers(output_indices, output_distances, k);
        auto icopy_ptr = ptrs.first;
        auto dcopy_ptr = ptrs.second;

        my_parent->my_index.get_nns_by_vector(query, k, get_search_k(k), icopy_ptr, dcopy_ptr);

        if (output_indices) {
            if constexpr(!same_internal_index) {
                output_indices->clear();
                output_indices->insert(output_indices->end(), my_indices.begin(), my_indices.end());
            }
        }

        if (output_distances) {
            if constexpr(!same_internal_data) {
                output_distances->clear();
                output_distances->insert(output_distances->end(), my_distances.begin(), my_distances.end());
            }
        }
    }

public:
    /**
     * @copydoc knncolle::Searcher::search() 
     */
    void search(const Float_* query, Index_ k, std::vector<Index_>* output_indices, std::vector<Float_>* output_distances) {
        if constexpr(same_internal_data) {
            search_raw(query, k, output_indices, output_distances);
        } else {
            std::copy_n(query, my_parent->my_dim, my_buffer.begin());
            search_raw(my_buffer.data(), k, output_indices, output_distances);
        }
    }
};

/**
 * @brief Prebuilt index for an Annoy search.
 *
 * Instances of this class are usually constructed using `AnnoyBuilder::build_raw()`.
 *
 * @tparam Distance_ An **Annoy** class to compute the distance between vectors, e.g., `Annoy::Euclidean`.
 * @tparam Dim_ Integer type for the number of dimensions.
 * For the output of `AnnoyBuilder::build_raw()`, this is set to `Matrix_::dimension_type`.
 * @tparam Index_ Integer type for the indices.
 * For the output of `AnnoyBuilder::build_raw()`, this is set to `Matrix_::index_type`.
 * @tparam Float_ Floating point type for the query data and output distances.
 * @tparam InternalIndex_ Integer type for the internal indices in Annoy.
 * @tparam InternalData_ Floating point type for the internal data in Annoy.
 */
template<class Distance_, typename Dim_, typename Index_, typename Float_, typename InternalIndex_, typename InternalData_>
class AnnoyPrebuilt : public knncolle::Prebuilt<Dim_, Index_, Float_> {
public:
    /**
     * @cond
     */
    template<class Matrix_>
    AnnoyPrebuilt(const Matrix_& data, const AnnoyOptions& options) :
        my_dim(data.num_dimensions()),
        my_obs(data.num_observations()),
        my_search_mult(options.search_mult),
        my_index(my_dim)
    {
        typedef typename Matrix_::data_type Data_;
        auto work = data.create_workspace();
        if constexpr(std::is_same<Data_, InternalData_>::value) {
            for (Index_ i = 0; i < my_obs; ++i) {
                auto ptr = data.get_observation(work);
                my_index.add_item(i, ptr);
            }
        } else {
            std::vector<InternalData_> incoming(my_dim);
            for (Index_ i = 0; i < my_obs; ++i) {
                auto ptr = data.get_observation(work);
                std::copy_n(ptr, my_dim, incoming.begin());
                my_index.add_item(i, incoming.data());
            }
        }

        my_index.build(options.num_trees);
        return;
    }
    /**
     * @endcond
     */

private:
    Dim_ my_dim;
    Index_ my_obs;
    double my_search_mult;
    Annoy::AnnoyIndex<InternalIndex_, InternalData_, Distance_, Annoy::Kiss64Random, Annoy::AnnoyIndexSingleThreadedBuildPolicy> my_index;

    friend class AnnoySearcher<Distance_, Dim_, Index_, Float_, InternalIndex_, InternalData_>;

public:
    /**
     * @copydoc knncolle::Prebuilt::num_dimensions() 
     */
    Dim_ num_dimensions() const {
        return my_dim;
    }

    /**
     * @copydoc knncolle::Prebuilt::num_observations() 
     */
    Index_ num_observations() const {
        return my_obs;
    }

    /**
     * Creates an `AnnoySearcher` instance.
     */
    std::unique_ptr<knncolle::Searcher<Index_, Float_> > initialize() const {
        return std::make_unique<AnnoySearcher<Distance_, Dim_, Index_, Float_, InternalIndex_, InternalData_> >(this);
    }
};

/**
 * @brief Perform an approximate nearest neighbor search with Annoy.
 *
 * In the Approximate Nearest Neighbors Oh Yeah (Annoy) algorithm, a tree is constructed where a random hyperplane splits the points into two subsets at each internal node.
 * Leaf nodes are defined when the number of points in a subset falls below a threshold (close to twice the number of dimensions for the settings used here).
 * Multiple trees are constructed in this manner, each of which is different due to the random choice of hyperplanes.
 * For a given query point, each tree is searched to identify the subset of all points in the same leaf node as the query point. 
 * The union of these subsets across all trees is exhaustively searched to identify the actual nearest neighbors to the query.
 *
 * @see
 * Bernhardsson E (2018).
 * Annoy.
 * https://github.com/spotify/annoy
 *
 * @tparam Distance_ An **Annoy** class to compute the distance between vectors, e.g., `Annoy::Euclidean`, `Annoy::Manhattan`.
 * Note that this is not the same as `knncolle::MockDistance`.
 * @tparam Matrix_ Matrix-like object satisfying the `knncolle::MockMatrix` interface.
 * @tparam Float_ Floating point type for the query data and output distances.
 * @tparam InternalIndex_ Integer type for the internal indices in Annoy.
 * @tparam InternalData_ Floating point type for the internal data in Annoy.
 * This defaults to a `float` instead of a `double` to sacrifice some accuracy for performance.
 */
template<
    class Distance_ = Annoy::Euclidean,
    class Matrix_ = knncolle::SimpleMatrix<int, int, double>, 
    typename Float_ = double, 
    typename InternalIndex_ = typename Matrix_::index_type, 
    typename InternalData_ = float>
class AnnoyBuilder : public knncolle::Builder<Matrix_, Float_> {
private:
    AnnoyOptions my_options;

public:
    /**
     * @param options Further options for Annoy index construction and searching.
     */
    AnnoyBuilder(AnnoyOptions options) : my_options(std::move(options)) {}

    /**
     * Default constructor.
     */
    AnnoyBuilder() = default;

    /**
     * @return Options to the Annoy algorithm,
     * to be modified prior to calling `build_raw()` and friends.
     */
    AnnoyOptions& get_options() {
        return my_options;
    }

public:
    /**
     * Creates an `AnnoyPrebuilt` instance.
     */
    knncolle::Prebuilt<typename Matrix_::dimension_type, typename Matrix_::index_type, Float_>* build_raw(const Matrix_& data) const {
        return new AnnoyPrebuilt<Distance_, typename Matrix_::dimension_type, typename Matrix_::index_type, Float_, InternalIndex_, InternalData_>(data, my_options);
    }
};

}

#endif
