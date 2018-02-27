#ifndef NODE_H
#define NODE_H

#include <string>
#include <vector>

class Node
{
public:
    Node();
    virtual ~Node() {}
    virtual int size() = 0;
    virtual void print(int indent) = 0;
};


class Document : public Node
{
public:
    Document(std::string name, std::string text);
    int size();
    void print(int indent);

private:
    std::string name;
    std::string text;
};


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


#endif // NODE_H
