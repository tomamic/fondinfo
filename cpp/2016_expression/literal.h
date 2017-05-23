#ifndef LITERAL_H
#define LITERAL_H

#include <string>
#include "expression.h"

class Literal : public Expression
{
private:
    float val_;
public:
    Literal(float val);
    float eval();
    std::string prefix();
};

#endif // LITERAL_H
