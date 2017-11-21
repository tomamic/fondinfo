//Illustrates the difference between a call-by-value
//parameter and a call-by-reference parameter.
#include <iostream>
using namespace std;

void doStuff(int par1Value, int* par2Ref);
//par1Value is a call-by-value formal parameter and
//par2Ref is a call-by-reference formal parameter.

int main( )
{
    int n1, n2;
       
    n1 = 1;
    n2 = 2;
    doStuff(n1, &n2);
    cout << "n1 after function call = " << n1 << endl;
    cout << "n2 after function call = " << n2 << endl;

    system("pause");
    return 0;
}

void doStuff(int par1Value, int* par2Ref)
{
    par1Value = 111;
    cout << "par1Value in function call = "
           << par1Value << endl;
    *par2Ref = 222;
    cout << "par2Ref in function call = "
           << *par2Ref << endl;
}
