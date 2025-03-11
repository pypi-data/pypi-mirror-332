// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_ARRAY_ARRAY2D_H_
#define LIB_INCLUDE_SPARKLEN_ARRAY_ARRAY2D_H_

#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <vector>

template <typename T> class SharedArray2D; // Forward declaration


template <typename T> class Array2D {

	private:

	size_t _size;
	T *_data;
	size_t _n_rows;
	size_t _n_cols;
	bool _ownData;

	public:

	// Default constructor
	Array2D();

	// Constructor with rows, columns, and optional external data
	Array2D(size_t n_rows, size_t n_cols, T *data = nullptr);

    // Copy constructor
    Array2D(const Array2D<T> &other);

    // Move constructor
    Array2D(Array2D<T> &&other) noexcept;

    // Destructor
    ~Array2D();

    // Copy assignment operator
    Array2D<T> &operator=(const Array2D<T> &other);

    // Move assignment operator
    Array2D<T> &operator=(Array2D<T> &&other) noexcept;

    // Access size, rows, columns, and data
    size_t size() const;
    size_t rows() const;
    size_t cols() const;
    T *data() const;

    // Print array
    void _print() const;

    // See ownership
    bool own() const;

    // Access elements
    T &operator[](const size_t i) const;
    T &operator()(const size_t i, const size_t j) const;

    // Arithmetic operations
    void operator+=(T scalar);
    void operator*=(T scalar);
    void operator/=(T scalar);

    // Array addition
    void add(const Array2D<T>& arr);

    // Friend class declaration for SharedArray
    friend class SharedArray2D<T>; // Declare SharedArray as a friend
};


// Default constructor
template <typename T> Array2D<T>::Array2D(){
	_n_rows = 0;
	_n_cols = 0;
	_size = 0;
	_data = nullptr;
	_ownData = false;
}

// Constructor with rows, columns, and optional external data
template <typename T> Array2D<T>::Array2D(size_t n_rows, size_t n_cols, T *data){
	_n_rows = n_rows;
	_n_cols = n_cols;
	_size = n_cols*n_rows;
	if (data==nullptr){
		_ownData = true;
		_data = new T[_size];
		for (size_t i=0; i<_size; i++){
			_data[i] = 0;
		}
	} else {
		_ownData = false;
		_data = data;
	}
}

// Copy constructor
template <typename T> Array2D<T>::Array2D(const Array2D<T> &other) {
    _n_rows = other._n_rows;
    _n_cols = other._n_cols;
    _size = other._size;
    _ownData = true;
    _data = new T[_size];
    std::copy(other._data, other._data + _size, _data);
}

// Move constructor
template <typename T> Array2D<T>::Array2D(Array2D<T>&& other) noexcept {
    _n_rows = other._n_rows;
    _n_cols = other._n_cols;
    _size = other._size;
    _data = other._data;
    _ownData = other._ownData;
    other._n_rows = 0;
    other._n_cols = 0;
    other._size = 0;
    other._data = nullptr;
    other._ownData = false;
}

// Destructor
template <typename T> Array2D<T>::~Array2D() {
    if (_ownData) {
        delete[] _data;
    }
}

// Copy assignment operator
template <typename T> Array2D<T> &Array2D<T>::operator=(const Array2D<T> &other) {
    if (this != &other) {
        if (_ownData) {
            delete[] _data;
        }
        _n_rows = other._n_rows;
        _n_cols = other._n_cols;
        _size = other._size;
        _data = new T[_size];
        _ownData = true;
        copy(other._data, other._data + _size, _data);
    }
    return *this;
}

// Move assignment operator
template <typename T> Array2D<T> &Array2D<T>::operator=(Array2D<T> &&other) noexcept {
    if (this != &other) {
        if (_ownData) {
            delete[] _data;
        }
        _n_rows = other._n_rows;
        _n_cols = other._n_cols;
        _size = other._size;
        _data = other._data;
        _ownData = other._ownData;
        other._n_rows = 0;
        other._n_cols = 0;
        other._size = 0;
        other._data = nullptr;
        other._ownData = false;
    }
    return *this;
}

// Access size of the array
template <typename T> size_t Array2D<T>::size() const {
    return _size;
}

// Access number of rows
template <typename T> size_t Array2D<T>::rows() const {
    return _n_rows;
}

// Access number of columns
template <typename T> size_t Array2D<T>::cols() const {
    return _n_cols;
}

// Access pointer to data
template <typename T> T *Array2D<T>::data() const {
    return _data;
}

// Print array elements
template <typename T> void Array2D<T>::_print() const{
	for (size_t i=0; i<_n_rows; i++){
		for (size_t j=0; j<_n_cols; j++){
			std::cout << " " << _data[i * _n_cols + j];
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}

// See ownership
template <typename T> bool Array2D<T>::own() const {
	return _ownData;
}

// Access elements with linear index
template <typename T> T &Array2D<T>::operator[](const size_t i) const {
    if (i >= _size) throw std::out_of_range("Index out of range");
    return _data[i];
}

// Access elements with row and column indices
template <typename T> T &Array2D<T>::operator()(const size_t i, const size_t j) const {
    if (i >= _n_rows || j >= _n_cols) throw std::out_of_range("Index out of range");
    return _data[i * _n_cols + j];
}

// Add scalar to each element
template <typename T> void Array2D<T>::operator+=(T scalar) {
    for (size_t i = 0; i < _size; ++i) {
        _data[i] += scalar;
    }
}

// Multiply each element by scalar
template <typename T> void Array2D<T>::operator*=(T scalar) {
    for (size_t i = 0; i < _size; ++i) {
        _data[i] *= scalar;
    }
}

// Divide each element by scalar
template <typename T> void Array2D<T>::operator/=(T scalar) {
    if (scalar == T()) throw std::invalid_argument("Division by zero.");
    for (size_t i = 0; i < _size; ++i) {
        _data[i] /= scalar;
    }
}

// Add another Array2D to this one
template <typename T> void Array2D<T>::add(const Array2D<T> &arr) {
    if (_n_rows == arr.rows() && _n_cols == arr.cols()) {
        for (size_t i = 0; i < _size; ++i) {
            _data[i] += arr.data()[i];
        }
    } else {
        throw std::invalid_argument("Arrays must have the same dimensions.");
    }
}


#define ARRAY_DEFINE_TYPE(TYPE, NAME)                 			\
  typedef Array2D<TYPE> Array##NAME##2D;                    	\
  typedef std::vector<Array##NAME##2D> ListArray##NAME##2D; 	\
  typedef std::vector<ListArray##NAME##2D> ListListArray##NAME##2D

ARRAY_DEFINE_TYPE(double, Double);
ARRAY_DEFINE_TYPE(int, Int);

#undef ARRAY_DEFINE_TYPE


#endif /* LIB_INCLUDE_SPARKLEN_ARRAY_ARRAY2D_H_ */
