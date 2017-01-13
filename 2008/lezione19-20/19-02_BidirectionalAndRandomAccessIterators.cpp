//Program to demonstrate bidirectional and random access iterators.
#include <iostream>
#include <vector>
using std::cout;
using std::endl;
using std::vector;

int main( )
{
    vector<char> container;

    container.push_back('A');
    container.push_back('B');
    container.push_back('C');
    container.push_back('D');   

    for (int i = 0; i < 4; i++)
        cout << "container[" << i << "] == " 
             << container[i] << endl;

    vector<char>::iterator p = container.begin( );
    cout << "The third entry is " << container[2] << endl;
    cout << "The third entry is " << p[2] << endl;
    cout << "The third entry is " << *(p + 2) << endl;

    cout << "Back to container[0].\n";
    p = container.begin( );
    cout << "which has value " << *p << endl;

    cout << "Two steps forward and one step back:\n";
    p++;
    cout << *p << endl;
    p++;
    cout << *p << endl;
    p--;
    cout << *p << endl;

    system("pause");
    return 0;
}
