#ifndef FLOATLIST_H
#define FLOATLIST_H

#include <iostream>
#include <stdexcept>

using namespace std;

struct Node {
    float val;
    Node* next;
};

class FloatList {
public:
    FloatList();
    FloatList(int size, float val);
    ~FloatList();
    float get(int pos);
    void set(int pos, float val);
    void push(float val);
    float pop();
    void insert(int pos, float val);
    float remove(int pos);
    int size();
    string str();
private:
    Node* head_;
    int size_;
};

#endif // FLOATLIST_H
