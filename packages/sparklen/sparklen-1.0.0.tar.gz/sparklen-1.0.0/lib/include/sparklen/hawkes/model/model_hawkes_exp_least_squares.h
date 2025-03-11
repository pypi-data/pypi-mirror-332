// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_HAWKES_MODEL_MODEL_HAWKES_EXP_LEAST_SQUARES_H_
#define LIB_INCLUDE_SPARKLEN_HAWKES_MODEL_MODEL_HAWKES_EXP_LEAST_SQUARES_H_

#include "sparklen/hawkes/model/model_hawkes_exp_least_squares_single.h"
#include <vector>


class ModelHawkesExpLeastSquares{

	private:

	size_t n_repetitions;

	size_t n_components;

	std::vector<ModelHawkesExpLeastSquaresSingle> multivariate_model;

	bool multivariate_model_computed; // when the model is agreagated, we can compute averaged loss and grad

	public:

	ModelHawkesExpLeastSquares();

	ModelHawkesExpLeastSquares(size_t n_rep, size_t n_comp);

	double compute_averaged_loss(const ListListSharedArrayDouble1D &list_jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta);

	SharedArrayDouble2D compute_averaged_grad(const ListListSharedArrayDouble1D &list_jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta);

	SharedArrayDouble2D compute_averaged_hessian(const ListListSharedArrayDouble1D &list_jump_times, const double end_time, const double decay);
};


#endif /* LIB_INCLUDE_SPARKLEN_HAWKES_MODEL_MODEL_HAWKES_EXP_LEAST_SQUARES_H_ */
