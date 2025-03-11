// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_PROX_PROX_ELASTIC_NET_H_
#define LIB_INCLUDE_SPARKLEN_PROX_PROX_ELASTIC_NET_H_

#include "sparklen/array/sharedarray.h"
#include "sparklen/array/sharedarray2D.h"

class ProxElasticNet{

	private:

	double l1_ratio;
	double penalization_const;
	size_t start;
	size_t end;
	bool positive;

	double apply_single(const double coeff, const double step_size);

	public:

	ProxElasticNet(double l1_r, double pen_const, size_t st, size_t ed, bool pos);

	void apply(SharedArrayDouble2D &x, const double step_size);
};

#endif /* LIB_INCLUDE_SPARKLEN_PROX_PROX_ELASTIC_NET_H_ */
