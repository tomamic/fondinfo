#include "sum.h"

Sum::Sum(Expression* e1, Expression* e2)
{
    e1_ = e1;
    e2_ = e2;
}

float Sum::eval()
{
    return e1_->eval() + e2_->eval();
}

std::string Sum::prefix()
{
    return "+ " + e1_->prefix() + " " + e2_->prefix();
}
