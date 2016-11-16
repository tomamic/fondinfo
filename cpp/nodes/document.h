#ifndef DOCUMENT_H
#define DOCUMENT_H

#include "node.h"
#include <string>
#include <iostream>

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

#endif // DOCUMENT_H
