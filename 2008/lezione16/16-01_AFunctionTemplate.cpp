//Program to demonstrate a function template.
#include <iostream>
using std::cout;
using std::endl;

//Interchanges the values of variable1 and variable2.
//The assignment operator must work for the type T.
template<class T>
void swapValues(T& variable1, T& variable2)
{
      T temp;

      temp = variable1;
      variable1 = variable2;
      variable2 = temp;
}

int main( )
{
    int integer1 = 1, integer2 = 2;
    cout << "Original integer values are "
         << integer1 << " " << integer2 << endl;
    swapValues(integer1, integer2);
    cout << "Swapped integer values are "
         << integer1 << " " << integer2 << endl;

    char symbol1 = 'A', symbol2 = 'B';
    cout << "Original character values are: "
         << symbol1 << " " << symbol2 << endl;
    swapValues(symbol1, symbol2);
    cout << "Swapped character values are: "
         << symbol1 << " " << symbol2 << endl;
    system("pause");
    return 0;
}
