#ifndef PRODUCT_H
#define PRODUCT_H

#include <string>
#include "expression.h"

class Product : public Expression
{
private:
    Expression* e1_;
    Expression* e2_;
public:
    Product(Expression* e1, Expression* e2);
    float eval();
    std::string prefix();
};

#endif // PRODUCT_H
