#ifndef INTVECTOR_H
#define INTVECTOR_H

#include <iostream>
#include <stdexcept>

using namespace std;

class IntVector {
public:
    IntVector();
    IntVector(int size, int val);
    ~IntVector();
    int get(int pos);
    void set(int pos, int val);
    void push(int val);
    int pop();
    void insert(int pos, int val);
    int remove(int pos);
    int size();
    string str();
private:
    int capacity_;
    int size_;
    int* data_;

    void expand_capacity();
};

#endif // INTVECTOR_H
