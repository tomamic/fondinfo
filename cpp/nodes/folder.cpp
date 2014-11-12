#include "folder.h"

using namespace std;

Folder::Folder(string name)
{
    this->name = name;
}

Folder::~Folder()
{
    clear();
}

void Folder::clear()
{
    while (subnodes.size() > 0) {
        delete_node(subnodes.size() - 1);
    }
}

int Folder::size()
{
    auto total_size = 0;
    for (auto n : subnodes) {
        total_size += n->size();
    }
    return total_size;
}

void Folder::print(int indent)
{
    for (auto i = 0; i < indent; ++i) cout << ' ';
    cout << name << endl;
    for (auto n : subnodes) {
        n->print(indent + 4);
    }
}

void Folder::add_node(Node* n)
{
    subnodes.push_back(n);
}

void Folder::delete_node(int index)
{
    if (0 <= index && index < subnodes.size()) {
        // 1. delete the node object from memory
        // 2. remove its pointer from the vector
        delete subnodes[index];
        subnodes.erase(begin(subnodes) + index);
    }
}
