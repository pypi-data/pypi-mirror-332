// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY2D_H_
#define LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY2D_H_

#include <memory>
#include <vector>
#include "sparklen/array/array2D.h"


template <typename T>
class SharedArray2D {
private:
    std::shared_ptr<Array2D<T>> _sharedPtr;
    bool _pythonOwner;

public:
    // Default constructor
    SharedArray2D();

    // Constructor with rows, columns, and optional external data
    SharedArray2D(size_t n_rows, size_t n_cols, T *data = nullptr);

    // Constructor with existing shared_ptr
    SharedArray2D(std::shared_ptr<Array2D<T>> sharedPtr);

    // Copy constructor
    SharedArray2D(const SharedArray2D<T> &other);

    // Move constructor
    SharedArray2D(SharedArray2D<T> &&other) noexcept;

    // Destructor
    virtual ~SharedArray2D();

    // Copy assignment operator
    SharedArray2D<T> &operator=(const SharedArray2D<T> &other);

    // Move assignment operator
    SharedArray2D<T> &operator=(SharedArray2D<T> &&other) noexcept;

    // Access elements operator
    T &operator()(const size_t i, const size_t j) const;

    // Get shared pointer
    std::shared_ptr<Array2D<T>> getSharedPtr() const;

    // Check if Python owns the data
    bool isPythonOwner() const;

    // Set Python ownership
    void setPythonOwner(bool owner);

    // Additional utility methods
    void reset();
    void swap(SharedArray2D<T> &other);

    // Utility methods
    size_t size() const;
    size_t rows() const;
    size_t cols() const;
    T *data() const;
    void _print() const;
    bool own() const;

    // Clear the shared array
    void clear();

    // Arithmetic operations
    void operator+=(T scalar);
    void operator*=(T scalar);
    void operator/=(T scalar);

    // Array addition
    void add(const SharedArray2D<T> &arr);
};

// Default constructor
template <typename T>
SharedArray2D<T>::SharedArray2D() : _sharedPtr(std::make_shared<Array2D<T>>()), _pythonOwner(false) {}

// Constructor with rows, columns, and optional external data
template <typename T>
SharedArray2D<T>::SharedArray2D(size_t n_rows, size_t n_cols, T *data)
    : _sharedPtr(std::make_shared<Array2D<T>>(n_rows, n_cols, data)), _pythonOwner(false) {}

// Constructor with existing shared_ptr
template <typename T>
SharedArray2D<T>::SharedArray2D(std::shared_ptr<Array2D<T>> sharedPtr) : _sharedPtr(sharedPtr), _pythonOwner(false) {}

// Copy constructor
template <typename T>
SharedArray2D<T>::SharedArray2D(const SharedArray2D<T> &other) : _sharedPtr(other._sharedPtr), _pythonOwner(other._pythonOwner) {}

// Move constructor
template <typename T>
SharedArray2D<T>::SharedArray2D(SharedArray2D<T> &&other) noexcept : _sharedPtr(std::move(other._sharedPtr)), _pythonOwner(other._pythonOwner) {
    other._pythonOwner = false;
}

// Destructor
template <typename T>
SharedArray2D<T>::~SharedArray2D() {}

// Copy assignment operator
template <typename T>
SharedArray2D<T> &SharedArray2D<T>::operator=(const SharedArray2D<T> &other) {
    if (this != &other) {
        _sharedPtr = other._sharedPtr;
        _pythonOwner = other._pythonOwner;
    }
    return *this;
}

// Move assignment operator
template <typename T>
SharedArray2D<T> &SharedArray2D<T>::operator=(SharedArray2D<T> &&other) noexcept {
    if (this != &other) {
        _sharedPtr = std::move(other._sharedPtr);
        _pythonOwner = other._pythonOwner;
        other._pythonOwner = false;
    }
    return *this;
}

// Access elements with row and column indices
template <typename T>
T &SharedArray2D<T>::operator()(const size_t i, const size_t j) const {
    return (*_sharedPtr)(i, j);
}

// Get shared pointer
template <typename T>
std::shared_ptr<Array2D<T>> SharedArray2D<T>::getSharedPtr() const {
    return _sharedPtr;
}

// Check if Python owns the data
template <typename T>
bool SharedArray2D<T>::isPythonOwner() const {
    return _pythonOwner;
}

// Set Python ownership
template <typename T>
void SharedArray2D<T>::setPythonOwner(bool owner) {
    _pythonOwner = owner;
}

// Reset shared pointer
template <typename T>
void SharedArray2D<T>::reset() {
    _sharedPtr.reset();
    _pythonOwner = false;
}

// Swap two SharedArray2D objects
template <typename T>
void SharedArray2D<T>::swap(SharedArray2D<T> &other) {
    std::swap(_sharedPtr, other._sharedPtr);
    std::swap(_pythonOwner, other._pythonOwner);
}

// Utility methods
template <typename T>
size_t SharedArray2D<T>::size() const {
    return _sharedPtr->size();
}

template <typename T>
size_t SharedArray2D<T>::rows() const {
    return _sharedPtr->rows();
}

template <typename T>
size_t SharedArray2D<T>::cols() const {
    return _sharedPtr->cols();
}

template <typename T>
T *SharedArray2D<T>::data() const {
    return _sharedPtr->data();
}

template <typename T>
void SharedArray2D<T>::_print() const {
    _sharedPtr->_print();
}

template <typename T>
bool SharedArray2D<T>::own() const {
    return _sharedPtr->own();
}

// Clear the shared array
template <typename T>
void SharedArray2D<T>::clear() {
    if (_sharedPtr->own() && !_pythonOwner) {
        _sharedPtr->_data = nullptr;
        _sharedPtr->_size = 0;
        _sharedPtr->_ownData = false;
    }
}

// Add scalar to each element
template <typename T>
void SharedArray2D<T>::operator+=(T scalar) {
    (*_sharedPtr) += scalar;
}

// Multiply each element by scalar
template <typename T>
void SharedArray2D<T>::operator*=(T scalar) {
    (*_sharedPtr) *= scalar;
}

// Divide each element by scalar
template <typename T>
void SharedArray2D<T>::operator/=(T scalar) {
    (*_sharedPtr) /= scalar;
}

// Add two SharedArray2D objects
template <typename T>
void SharedArray2D<T>::add(const SharedArray2D<T> &arr) {
    _sharedPtr->add(*arr._sharedPtr);
}

#define ARRAY_DEFINE_TYPE(TYPE, NAME)                 			\
  typedef SharedArray2D<TYPE> SharedArray##NAME##2D;                    	\
  typedef std::vector<SharedArray##NAME##2D> ListSharedArray##NAME##2D; 	\
  typedef std::vector<ListSharedArray##NAME##2D> ListListSharedArray##NAME##2D

ARRAY_DEFINE_TYPE(double, Double);
ARRAY_DEFINE_TYPE(int, Int);

#undef ARRAY_DEFINE_TYPE



#endif /* LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY2D_H_ */
