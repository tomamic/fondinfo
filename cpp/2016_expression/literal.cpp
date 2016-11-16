#include "literal.h"
#include <sstream>

using namespace std;

Literal::Literal(float val)
{
    val_ = val;
}

float Literal::eval()
{
    return val_;
}

string Literal::prefix()
{
    ostringstream out;
    out << val_;
    return out.str();
}

