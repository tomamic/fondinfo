//Program to demonstrate the template class PFArray.
#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;

#include "pfarray.h"
#include "pfarray.cpp"
using PFArraySavitch::PFArray;

int main( )
{
    PFArray<int> a(10);

    cout << "Enter up to 10 nonnegative integers.\n";
    cout << "Place a negative number at the end.\n";
    int next;
    cin >> next;
    while ((next >= 0) && (!a.full( )))
    {
        a.addElement(next);
        cin >> next;
    }
    if (next >= 0)
    {
        cout << "Could not read all numbers.\n";
        //Clear the unread input:
        while (next >= 0)
            cin >> next;
    }

    cout << "You entered the following:\n";
    int index;
    int count = a.getNumberUsed( );
    for (index = 0; index < count; index++)
        cout << a[index] << " ";
    cout << endl;

    PFArray<string> b(3);

    cout << "Enter three words:\n";
    string nextWord;
    for (index = 0; index < 3; index++)
    {
        cin >> nextWord;
        b.addElement(nextWord);
    }

    cout << "You wrote the following:\n";
    count = b.getNumberUsed( );
    for (index = 0; index < count; index++)
        cout << b[index] << " ";
    cout << endl;
    cout << "I hope you really mean it.\n";

    system("pause");
    return 0;
}
