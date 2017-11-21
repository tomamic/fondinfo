#ifndef FLOATVECTOR_H
#define FLOATVECTOR_H

#include <iostream>
#include <stdexcept>

using namespace std;

class FloatVector {
public:
    FloatVector();
    FloatVector(int size, float val);
    ~FloatVector();
    float get(int pos);
    void set(int pos, float val);
    void push(float val);
    float pop();
    void insert(int pos, float val);
    float remove(int pos);
    int size();
    string str();
private:
    int capacity_;
    int size_;
    float* data_;

    void expand_capacity();
};

#endif // FLOATVECTOR_H
