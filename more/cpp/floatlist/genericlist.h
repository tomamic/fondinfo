#ifndef GENERICLIST_H
#define GENERICLIST_H

#include <iostream>
#include <stdexcept>
#include <sstream>
#include <iomanip>

using namespace std;

template<class T>
struct GenericNode {
    T val;
    GenericNode<T>* next;
};

template<class T>
class GenericList {
public:
    GenericList();
    GenericList(int size, T val);
    ~GenericList();
    T get(int pos);
    void set(int pos, T val);
    void push(T val);
    T pop();
    void insert(int pos, T val);
    T remove(int pos);
    int size();
    string str();
private:
    GenericNode<T>* head_;
    int size_;
};


template<class T>
GenericList<T>::GenericList() {
    head_ = nullptr;
    size_ = 0;
}

template<class T>
GenericList<T>::GenericList(int size, T val) {
    head_ = nullptr;
    for (int i = 0; i < size; ++i) {
        head_ = new GenericNode<T>{val, head_};
    }
    size_ = size;
}

template<class T>
GenericList<T>::~GenericList() {
    while (size_ > 0) {
        remove(0);
    }
}

template<class T>
T GenericList<T>::get(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    GenericNode<T>* n = head_;
    for (int i = 0; i < pos; ++i) {
        n = n->next;
    }
    return n->val;
}

template<class T>
void GenericList<T>::set(int pos, T val) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    GenericNode<T>* n = head_;
    for (int i = 0; i < pos; ++i) {
        n = n->next;
    }
    n->val = val;
}

template<class T>
void GenericList<T>::push(T val) {
    insert(size_, val);
}

template<class T>
T GenericList<T>::pop() {
    return remove(size_ - 1);
}

template<class T>
void GenericList<T>::insert(int pos, T val) {
    if (pos < 0 || pos > size_) {
        throw out_of_range("wrong pos");
    }
    if (pos == 0) {
        head_ = new GenericNode<T>{val, head_};
    } else {
        GenericNode<T>* n = head_;
        for (int i = 0; i < pos - 1; ++i) {
            n = n->next;
        }
        n->next = new GenericNode<T>{val, n->next};
    }
    ++size_;
}

template<class T>
T GenericList<T>::remove(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    GenericNode<T>* n = head_;
    if (pos == 0) {
        head_ = n->next;
    } else {
        for (int i = 0; i < pos - 1; ++i) {
            n = n->next;
        }
        GenericNode<T>* prev = n;
        n = n->next;
        prev->next = n->next;
    }
    --size_;
    T val = n->val;
    delete n;
    return val;
}

template<class T>
string GenericList<T>::str() {
    ostringstream out;
    GenericNode<T>* n = head_;
    while (n != nullptr) {
        out << n->val;
        if (n->next != nullptr) {
            out << ' ';
        }
        n = n->next;
    }
    return out.str();
}


template<class T>
int GenericList<T>::size() {
    return size_;
}

#endif // GENERICLIST_H
