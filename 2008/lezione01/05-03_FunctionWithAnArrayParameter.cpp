//Demonstrates an array parameter.
#include <iostream>
using namespace std;

void fillUp(int a[], int size);
//Precondition: size is the declared size of the array a.
//The user will type in size integers.
//Postcondition: The array a is filled with size integers
//from the keyboard.

int main( )
{
    int a[5], b[10];

    fillUp(a, 5);
    fillUp(b, 10);

    return 0;
}

void fillUp(int a[], int size)
{
    cout << "Enter " << size << " numbers:\n";
    for (int i = 0; i < size; i++)
        cin >> a[i];
    cout << "The last array index used is " << (size - 1) << endl;
}
