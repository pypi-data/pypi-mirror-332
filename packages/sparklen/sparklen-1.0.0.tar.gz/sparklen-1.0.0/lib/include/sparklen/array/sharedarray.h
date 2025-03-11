// Author : Romain E. Lacoste
// License : BSD-3-Clause

#ifndef LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY_H_
#define LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY_H_


#include <memory>
#include <vector>
#include "sparklen/array/array.h"

template <typename T> class SharedArray {
private:
    std::shared_ptr<Array<T>> _sharedPtr;
    bool _pythonOwner;

public:
    // Default constructor
    SharedArray();

    // Constructor with size and optional external data
    SharedArray(size_t size, T *data=nullptr);

    // Constructor with existing shared_ptr
    SharedArray(std::shared_ptr<Array<T>> sharedPtr);

    // Copy constructor
    SharedArray(const SharedArray<T> &other);

    // Move constructor
    SharedArray(SharedArray<T> &&other) noexcept;

    // Destructor
    virtual ~SharedArray();

    // Copy assignment operator
    SharedArray<T> &operator=(const SharedArray<T> &other);

    // Move assignment operator
    SharedArray<T> &operator=(SharedArray<T> &&other) noexcept;

    // Access elements operator
    T &operator[](const size_t i) const;

    // Get shared pointer
    std::shared_ptr<Array<T>> getSharedPtr() const;

    // Check if Python owns the data
    bool isPythonOwner() const;

    // Set Python ownership
    void setPythonOwner(bool owner);

    // Additional utility methods
    void reset();
    void swap(SharedArray<T> &other);

    // Utility methods
    size_t size() const;
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
    void add(const SharedArray<T> &arr);
};

// Default constructor
template <typename T>
SharedArray<T>::SharedArray() {
    _sharedPtr = std::make_shared<Array<T>>();
    _pythonOwner = false;
}

// Constructor with size and optional external data
template <typename T>
SharedArray<T>::SharedArray(size_t size, T *data) {
    _sharedPtr = std::make_shared<Array<T>>(size, data);
    _pythonOwner = false;
}

// Constructor with existing shared_ptr
template <typename T>
SharedArray<T>::SharedArray(std::shared_ptr<Array<T>> sharedPtr) {
    _sharedPtr = sharedPtr;
    _pythonOwner = false;
}

// Copy constructor
template <typename T>
SharedArray<T>::SharedArray(const SharedArray<T> &other) {
    _sharedPtr = other._sharedPtr;
    _pythonOwner = other._pythonOwner;
}
// Move constructor
template <typename T>
SharedArray<T>::SharedArray(SharedArray<T> &&other) noexcept {
    _sharedPtr = std::move(other._sharedPtr);
    _pythonOwner = other._pythonOwner;
    other._pythonOwner = false;
}

// Destructor
template <typename T>
SharedArray<T>::~SharedArray() {}

// Copy assignment operator
template <typename T>
SharedArray<T> &SharedArray<T>::operator=(const SharedArray<T> &other) {
    if (this != &other) {
        _sharedPtr = other._sharedPtr;
        _pythonOwner = other._pythonOwner;
    }
    return *this;
}

// Move assignment operator
template <typename T>
SharedArray<T> &SharedArray<T>::operator=(SharedArray<T> &&other) noexcept {
    if (this != &other) {
        _sharedPtr = std::move(other._sharedPtr);
        _pythonOwner = other._pythonOwner;
        other._pythonOwner = false;
    }
    return *this;
}

// Access elements
template <typename T>
T &SharedArray<T>::operator[](const size_t i) const {
    return (*_sharedPtr)[i];
}

// Get shared pointer
template <typename T>
std::shared_ptr<Array<T>> SharedArray<T>::getSharedPtr() const {
    return _sharedPtr;
}

// Check if Python owns the data
template <typename T>
bool SharedArray<T>::isPythonOwner() const {
    return _pythonOwner;
}

// Set Python ownership
template <typename T>
void SharedArray<T>::setPythonOwner(bool owner) {
    _pythonOwner = owner;
}

// Reset shared pointer
template <typename T>
void SharedArray<T>::reset() {
    _sharedPtr.reset();
    _pythonOwner = false;
}

// Swap two SharedArray objects
template <typename T>
void SharedArray<T>::swap(SharedArray<T> &other) {
    std::swap(_sharedPtr, other._sharedPtr);
    std::swap(_pythonOwner, other._pythonOwner);
}

// Utility methods
template <typename T>
size_t SharedArray<T>::size() const {
    return _sharedPtr->size();
}

template <typename T>
T *SharedArray<T>::data() const {
    return _sharedPtr->data();
}

template <typename T>
void SharedArray<T>::_print() const {
    _sharedPtr->_print();
}

template <typename T>
bool SharedArray<T>::own() const {
    return _sharedPtr->own();
}

// Add scalar to each element
template <typename T>
void SharedArray<T>::operator+=(T scalar) {
    (*_sharedPtr) += scalar;
}

// Multiply each element by scalar
template <typename T>
void SharedArray<T>::operator*=(T scalar) {
    (*_sharedPtr) *= scalar;
}

// Divide each element by scalar
template <typename T>
void SharedArray<T>::operator/=(T scalar) {
    (*_sharedPtr) /= scalar;
}

// Add two SharedArray objects
template <typename T>
void SharedArray<T>::add(const SharedArray<T> &arr) {
    _sharedPtr->add(*arr._sharedPtr);
}

template <typename T>
void SharedArray<T>::clear() {
    // Ensure we only delete the data if we own it and it's not managed by NumPy
    if (_sharedPtr->own() && !_pythonOwner) {
        // Directly reset the internal state of Array<T>
        _sharedPtr->_data = nullptr; // Reset data pointer
        _sharedPtr->_size = 0;       // Reset size
        _sharedPtr->_ownData = false; // Reset ownership
    }
}

#define SHAREDARRAY_DEFINE_TYPE(TYPE, NAME)                 \
  typedef SharedArray<TYPE> SharedArray##NAME##1D;                    \
  typedef std::vector<SharedArray##NAME##1D> ListSharedArray##NAME##1D;    \
  typedef std::vector<ListSharedArray##NAME##1D> ListListSharedArray##NAME##1D;

SHAREDARRAY_DEFINE_TYPE(double, Double);

#undef SHAREDARRAY_DEFINE_TYPE


#endif /* LIB_INCLUDE_SPARKLEN_ARRAY_SHAREDARRAY_H_ */
