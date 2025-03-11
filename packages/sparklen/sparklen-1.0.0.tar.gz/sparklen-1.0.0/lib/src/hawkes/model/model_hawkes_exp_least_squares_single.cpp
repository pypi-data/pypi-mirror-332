// Author : Romain E. Lacoste
// License : BSD-3-Clause

#include "sparklen/hawkes/model/model_hawkes_exp_least_squares_single.h"
#include <math.h>

// Constructor
ModelHawkesExpLeastSquaresSingle::ModelHawkesExpLeastSquaresSingle(){
	n_components = 0;
	weights_computed = false;
	N = ArrayInt1D(n_components);
	H = ArrayDouble1D(n_components);
	H2 = ArrayDouble1D(n_components);
	D = ArrayDouble2D(n_components, n_components);
	C = ArrayDouble2D(n_components, n_components);
}

ModelHawkesExpLeastSquaresSingle::ModelHawkesExpLeastSquaresSingle(size_t n){
	n_components = n;
	weights_computed = false;
	N = ArrayInt1D(n_components);
	H = ArrayDouble1D(n_components);
	H2 = ArrayDouble1D(n_components);
	D = ArrayDouble2D(n_components, n_components);
	C = ArrayDouble2D(n_components, n_components);
}

size_t ModelHawkesExpLeastSquaresSingle::get_n_components(){
	return n_components;
}

void ModelHawkesExpLeastSquaresSingle::compute_weights(const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay){

	for (size_t j=0; j<n_components; ++j){
		const SharedArrayDouble1D &jump_times_j = jump_times[j];
		N[j] = jump_times_j.size();
		for (size_t j2=0; j2<n_components; ++j2){
			const SharedArrayDouble1D &jump_times_j2 = jump_times[j2];
			for (size_t h=0; h<jump_times_j.size(); ++h){
				size_t h2 = 0;
				double term = 0.;
				while (h2 < jump_times_j2.size() && jump_times_j2[h2] <jump_times_j[h]){
					term += decay*(exp(-decay*(jump_times_j[h]-jump_times_j2[h2])));
					h2++;
				}
				D(j,j2) += term;
				C(j,j2) += (1-exp(-2*decay*(end_time-jump_times_j[h])))*term;
			}
		}
		for (size_t h=0; h<jump_times_j.size(); ++h){
			H[j] += 1-exp(-decay*(end_time-jump_times_j[h]));
			H2[j] += 1-exp(-2*decay*(end_time-jump_times_j[h]));
		}
		H2[j] *= decay/2;
	}

	weights_computed = true;
}

double ModelHawkesExpLeastSquaresSingle::compute_loss_i(const size_t i, const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta){

	double ls_contrast_value_i{0.};

	double term_square{0.};
	double term_cross_mu{0.};
	double term_stieltjes{0.};
	double term_cross_A{0.};

	ls_contrast_value_i += theta(i,0)*theta(i,0)*end_time - 2*theta(i,0)*N[i];

	for (size_t j=0; j<n_components; ++j){
		term_square += theta(i,j+1)*theta(i,j+1)*H2[j];
		term_cross_mu += theta(i,j+1)*H[j];
		term_stieltjes += theta(i,j+1)*D(i,j);
		for (size_t j2=0; j2<n_components; ++j2){
			term_cross_A += theta(i,j+1)*theta(i,j2+1)*C(j,j2);
		}
	}
	ls_contrast_value_i += term_square + 2*theta(i,0)*term_cross_mu - 2*term_stieltjes + term_cross_A;

	return ls_contrast_value_i;
}

double ModelHawkesExpLeastSquaresSingle::compute_loss(const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta){

	double loss{0.};

	if (!weights_computed){
		compute_weights(jump_times, end_time, decay);
	}

	for (size_t i=0; i<n_components; ++i){
		loss += ModelHawkesExpLeastSquaresSingle::compute_loss_i(i, jump_times, end_time, decay, theta);
	}
	loss /= end_time;
	return loss;
}

void ModelHawkesExpLeastSquaresSingle::compute_grad_i(const size_t i, const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta, SharedArrayDouble2D &grad){


	grad(i,0) = 2*(theta(i,0)*end_time - N[i]);

	for (size_t j=0; j<n_components; ++j){
		grad(i,0) += 2*theta(i,j+1)*H[j];
		grad(i,j+1) = 2*theta(i,j+1)*H2[j] + 2*theta(i,j+1)*C(j,j) + 2*theta(i,0)*H[j] - 2*D(i,j);

		for (size_t j2=0; j2<n_components; ++j2){
			if (j2 != j){
				grad(i,j+1) += theta(i,j2+1)*(C(j,j2)+C(j2,j));
			}
		}
	}
}

SharedArrayDouble2D ModelHawkesExpLeastSquaresSingle::compute_grad(const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay, const SharedArrayDouble2D &theta){

	SharedArrayDouble2D grad(n_components, n_components+1);

	if (!weights_computed){
		compute_weights(jump_times, end_time, decay);
	}

	for (size_t i=0; i<n_components; ++i){
		ModelHawkesExpLeastSquaresSingle::compute_grad_i(i, jump_times, end_time, decay, theta, grad);
	}
	grad /= end_time;
	return grad;
}

SharedArrayDouble2D ModelHawkesExpLeastSquaresSingle::compute_hessian(const ListSharedArrayDouble1D &jump_times, const double end_time, const double decay){

	SharedArrayDouble2D hessian(n_components+1, n_components+1);
	if (!weights_computed){
		compute_weights(jump_times, end_time, decay);
	}

	hessian(0,0) = 2.*end_time;

	for (size_t j=0; j<n_components; ++j){
		hessian(0,j) = 2*H[j];
		hessian(j,0) = 2*H[j];
	}

	for (size_t j=0; j<n_components; ++j){
		for (size_t j2=0; j2<n_components; ++j2){
			hessian(j+1,j2+1) = C(j,j2)+C(j2,j);
			if (j==j2){
				hessian(j+1,j2+1) += 2*H2[j];
			}
		}
	}
	hessian /= end_time;

	return hessian;
}

