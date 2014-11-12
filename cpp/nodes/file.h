#ifndef FILE_H
#define FILE_H

#include "node.h"
#include <string>
#include <iostream>

class File : public Node
{
public:
    File(std::string name, std::string text);
    int size();
    void print(int indent);

private:
    std::string name;
    std::string text;
};

#endif // FILE_H
