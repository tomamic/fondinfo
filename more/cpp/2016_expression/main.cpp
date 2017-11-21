#include <iostream>
#include "sum.h"
#include "product.h"
#include "literal.h"

using namespace std;

int main(int argc, char *argv[])
{
    auto prod1 = new Product(new Literal(3), new Literal(2));
    auto sum1 = new Sum(new Literal(4), prod1);
    auto prod2 = new Product(new Literal(5), sum1);

    cout << prod2->eval() << endl;
    cout << prod2->prefix() << endl;

    return 0;
}
