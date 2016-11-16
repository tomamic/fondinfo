#include "product.h"

Product::Product(Expression* e1, Expression* e2)
{
    e1_ = e1;
    e2_ = e2;
}

float Product::eval()
{
    return e1_->eval() * e2_->eval();
}

std::string Product::prefix()
{
    return "* " + e1_->prefix() + " " + e2_->prefix();
}
