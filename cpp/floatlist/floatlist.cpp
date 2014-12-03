#include <sstream>
#include <iomanip>
#include "floatlist.h"

FloatList::FloatList() {
    head_ = nullptr;
    size_ = 0;
}

FloatList::FloatList(int size, float val) {
    head_ = nullptr;
    for (int i = 0; i < size; ++i) {
        head_ = new Node{val, head_};
    }
    size_ = size;
}

FloatList::~FloatList() {
    while (size_ > 0) {
        remove(0);
    }
}

float FloatList::get(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    Node* n = head_;
    for (int i = 0; i < pos; ++i) {
        n = n->next;
    }
    return n->val;
}

void FloatList::set(int pos, float val) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    Node* n = head_;
    for (int i = 0; i < pos; ++i) {
        n = n->next;
    }
    n->val = val;
}

void FloatList::push(float val) {
    insert(size_, val);
}

float FloatList::pop() {
    return remove(size_ - 1);
}

void FloatList::insert(int pos, float val) {
    if (pos < 0 || pos > size_) {
        throw out_of_range("wrong pos");
    }
    if (pos == 0) {
        head_ = new Node{val, head_};
    } else {
        Node* n = head_;
        for (int i = 0; i < pos - 1; ++i) {
            n = n->next;
        }
        n->next = new Node{val, n->next};
    }
    ++size_;
}

float FloatList::remove(int pos) {
    if (pos < 0 || pos >= size_) {
        throw out_of_range("wrong pos");
    }
    Node* n = head_;
    if (pos == 0) {
        head_ = n->next;
    } else {
        for (int i = 0; i < pos - 1; ++i) {
            n = n->next;
        }
        Node* prev = n;
        n = n->next;
        prev->next = n->next;
    }
    --size_;
    float val = n->val;
    delete n;
    return val;
}

string FloatList::str() {
    ostringstream out;
    Node* n = head_;
    while (n != nullptr) {
        out << fixed << setprecision(1) << n->val;
        if (n->next != nullptr) {
            out << ' ';
        }
        n = n->next;
    }
    return out.str();
}


int FloatList::size() {
    return size_;
}
