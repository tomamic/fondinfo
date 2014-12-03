#include <sstream>
#include <iomanip>
#include "floatvector.h"

using namespace std;

FloatVector::FloatVector() {
    capacity_ = 8;
    data_ = new float[capacity_];
    size_ = 0;
}

FloatVector::FloatVector(int size, float val) {
    capacity_ = size;
    data_ = new float[capacity_];
    size_ = size;
    for (int i = 0; i < size_; ++i) {
        data_[i] = val;
    }
}

FloatVector::~FloatVector() {
    delete[] data_;
}

float FloatVector::get(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    return data_[pos];
}


void FloatVector::set(int pos, float val) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    data_[pos] = val;
}

void FloatVector::push(float val) {
    insert(size_, val);
}

float FloatVector::pop() {
    return remove(size_ - 1);
}

void FloatVector::insert(int pos, float val) {
    if (pos < 0 || pos > size_) {
        throw out_of_range("wrong pos");
    }
    if (size_ == capacity_) {
        expand_capacity();
    }
    for (int i = size_; i > pos; --i) {
        data_[i] = data_[i - 1];
    }
    data_[pos] = val;
    ++size_;
}

float FloatVector::remove(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    float val = data_[pos];
    --size_;
    for (int i = pos; i < size_; ++i) {
        data_[i] = data_[i + 1];
    }
    return val;
}

int FloatVector::size() {
    return size_;
}

string FloatVector::str() {
    ostringstream out;
    for (int i = 0; i < size_; ++i) {
        out << data_[i];
        if (i < size_ - 1) {
            out << ' ';
        }
    }
    return out.str();
}

void FloatVector::expand_capacity() {
    capacity_ *= 2;
    float* bigger = new float[capacity_];
    for (int i = 0; i < size_; i++) {
        bigger[i] = data_[i];
    }
    delete[] data_;
    data_ = bigger;
}

