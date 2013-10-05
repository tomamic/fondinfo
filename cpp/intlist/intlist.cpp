#include <sstream>
#include "intlist.h"

IntList::IntList() {
    head_ = nullptr;
    size_ = 0;
}

IntList::IntList(int size, int val) {
    head_ = nullptr;
    for (int i = 0; i < size; ++i) {
        head_ = new Node{val, head_};
    }
    size_ = size;
}

int IntList::get(int pos) {
    if (pos < 0 || pos >= size_) throw out_of_range("wrong pos");
    Node* n = head_;
    for (int i = 0; i < pos; ++i) n = n->next;
    return n->val;
}

void IntList::set(int pos, int val) {
    if (pos < 0 || pos >= size_) throw out_of_range("wrong pos");
    Node* n = head_;
    for (int i = 0; i < pos; ++i) n = n->next;
    n->val = val;
}

void IntList::push(int val) {
    insert(size_, val);
}

int IntList::pop() {
    return remove(size_ - 1);
}

void IntList::insert(int pos, int val) {
    if (pos < 0 || pos > size_) throw out_of_range("wrong pos");
    if (pos == 0) {
        head_ = new Node{val, head_};
    } else {
        Node* n = head_;
        for (int i = 0; i < pos - 1; ++i) n = n->next;
        n->next = new Node{val, n->next};
    }
    ++size_;
}

int IntList::remove(int pos) {
    if (pos < 0 || pos >= size_) throw out_of_range("wrong pos");
    Node* x = head_;
    if (pos == 0) {
        head_ = head_->next;
    } else {
        Node* n = head_;
        for (int i = 0; i < pos - 1; ++i) n = n->next;
        x = n->next;
        n->next = x->next;
    }
    --size_;
    int val = x->val;
    delete x;
    return val;
}

string IntList::str() {
    ostringstream out;
    Node* n = head_;
    while (n != nullptr) {
        out << n->val;
        if (n->next != nullptr) out << ' ';
        n = n->next;
    }
    return out.str();
}


int IntList::size() {
    return size_;
}
