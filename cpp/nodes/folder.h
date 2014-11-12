#ifndef FOLDER_H
#define FOLDER_H

#include <vector>
#include <iostream>
#include "node.h"

class Folder : public Node
{
public:
    Folder(std::string name);
    ~Folder();
    void clear();
    int size();
    void print(int indent);
    void add_node(Node* n);
    void delete_node(int index);
private:
    std::string name;
    std::vector<Node*> subnodes;
};

#endif // FOLDER_H
