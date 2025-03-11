// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_PROX_PROX_ZERO_H_
#define LIB_INCLUDE_SPARKLEN_PROX_PROX_ZERO_H_

#include "sparklen/array/sharedarray.h"
#include "sparklen/array/sharedarray2D.h"

class ProxZero{

	private:

	double penalization_const;
	size_t start;
	size_t end;
	bool positive;

	double apply_single(const double coeff, const double step_size);

	public:

	ProxZero(double pen_const, size_t st, size_t ed, bool pos);

	void apply(SharedArrayDouble2D &x, const double step_size);
};

#endif /* LIB_INCLUDE_SPARKLEN_PROX_PROX_ZERO_H_ */
