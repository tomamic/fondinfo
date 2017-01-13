#include <iostream>
#include <cstdlib>
using std::cin;
using std::cout;
using std::endl;

class DivideByZero
{};

double safeDivide(int top, int bottom) throw (DivideByZero);

int main( )
{
    int numerator;
    int denominator;
    double quotient;
    cout << "Enter numerator:\n"; 
    cin >> numerator;
    cout << "Enter denominator:\n";
    cin >> denominator;

    try
    {
       quotient = safeDivide(numerator, denominator);
    }
    catch(DivideByZero)
    {
         cout << "Error: Division by zero!\n"
              << "Program aborting.\n";
         exit(0);
    }

    cout << numerator << "/" << denominator 
         << " = " << quotient << endl;

    cout << "End of program.\n";
    return 0;
}


double safeDivide(int top, int bottom) throw (DivideByZero)
{
    if (bottom == 0)
        throw DivideByZero( );

    return top/static_cast<double>(bottom);
}
