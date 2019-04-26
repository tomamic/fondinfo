#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Node {
public:
    virtual ~Node() {}
    virtual int size() = 0;
    virtual void print(int indent) = 0;
};


class Document : public Node {
public:
    Document(std::string name, std::string text) {
        this->name = name;
        this->text = text;
    }

    int size() {
        return text.size();
    }

    void print(int indent) {
        for (auto i = 0; i < indent; ++i) std::cout << ' ';
        std::cout << name << std::endl;
    }

private:
    std::string name;
    std::string text;
};


class Folder : public Node
{
public:
    Folder(std::string name) {
        this->name = name;
    }

    ~Folder() {
        clear();
    }

    void clear() {
        while (subnodes.size() > 0) {
            delete_node(subnodes.size() - 1);
        }
    }

    int size() {
        auto total_size = 0;
        for (auto n : subnodes) {
            total_size += n->size();
        }
        return total_size;
    }

    void print(int indent) {
        for (auto i = 0; i < indent; ++i) std::cout << ' ';
        std::cout << name << std::endl;
        for (auto n : subnodes) {
            n->print(indent + 4);
        }
    }

    void add_node(Node* n) {
        subnodes.push_back(n);
    }

    void delete_node(int index) {
        if (0 <= index && index < subnodes.size()) {
            // 1. delete the node object from memory
            // 2. remove its pointer from the vector
            delete subnodes[index];
            subnodes.erase(begin(subnodes) + index);
        }
    }

private:
    string name;
    vector<Node*> subnodes;
};

#endif // NODE_H
