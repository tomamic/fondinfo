#include <sstream>
#include "intvector.h"

using namespace std;

IntVector::IntVector() {
    capacity_ = 8;
    data_ = new int[capacity_];
    size_ = 0;
}

IntVector::IntVector(int size, int val) {
    capacity_ = size;
    data_ = new int[capacity_];
    size_ = size;
    for (int i = 0; i < size_; ++i) {
        data_[i] = val;
    }
}

IntVector::~IntVector() {
    delete[] data_;
}

int IntVector::get(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    return data_[pos];
}


void IntVector::set(int pos, int val) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    data_[pos] = val;
}

void IntVector::push(int val) {
    insert(size_, val);
}

int IntVector::pop() {
    return remove(size_ - 1);
}

void IntVector::insert(int pos, int val) {
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

int IntVector::remove(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    int val = data_[pos];
    --size_;
    for (int i = pos; i < size_; ++i) {
        data_[i] = data_[i + 1];
    }
    return val;
}

int IntVector::size() {
    return size_;
}

string IntVector::str() {
    ostringstream out;
    for (int i = 0; i < size_; ++i) {
        out << data_[i];
        if (i < size_ - 1) {
            out << ' ';
        }
    }
    return out.str();
}

void IntVector::expand_capacity() {
    capacity_ *= 2;
    int* bigger = new int[capacity_];
    for (int i = 0; i < size_; i++) {
        bigger[i] = data_[i];
    }
    delete[] data_;
    data_ = bigger;
}

