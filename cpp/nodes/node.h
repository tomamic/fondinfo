#ifndef NODE_H
#define NODE_H

class Node
{
public:
    Node();
    virtual ~Node() {}
    virtual int size() = 0;
    virtual void print(int indent) = 0;
};

#endif // NODE_H
