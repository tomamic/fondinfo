#ifndef INTLIST_H
#define INTLIST_H

#include <iostream>
#include <stdexcept>

using namespace std;

struct Node {
    int val;
    Node* next;
};

class IntList {
public:
    IntList();
    IntList(int size, int val);
    int get(int pos);
    void set(int pos, int val);
    void push(int val);
    int pop();
    void insert(int pos, int val);
    int remove(int pos);
    int size();
    string str();
private:
    Node* head_;
    int size_;
};

#endif // INTLIST_H
