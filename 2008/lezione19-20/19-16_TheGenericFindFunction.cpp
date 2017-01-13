//Program to demonstrate use of the generic find function. 
#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::find;

int main( )
{
    vector<char> line;

    cout << "Enter a line of text:\n";
    char next;
    cin.get(next);
    while (next != '\n')
    {
        line.push_back(next);
        cin.get(next);
    }

    vector<char>::const_iterator where;
    where = find(line.begin( ), line.end( ), 'e');
    //where is located at the first occurrence of 'e' in v.

    vector<char>::const_iterator p;
    cout << "You entered the following before you entered your first e:\n";
    for (p = line.begin( ); p != where; p++)
        cout << *p;
    cout << endl;

    cout << "You entered the following after that:\n";
    for (p = where; p != line.end( ); p++)
        cout << *p;
    cout << endl;

    cout << "End of demonstration.\n";
    system("pause");
    return 0;
}
