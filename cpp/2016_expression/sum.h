#ifndef SUM_H
#define SUM_H

#include <string>
#include "expression.h"

class Sum : public Expression
{
private:
    Expression* e1_;
    Expression* e2_;
public:
    Sum(Expression* e1, Expression* e2);
    float eval();
    std::string prefix();
};

#endif // SUM_H
