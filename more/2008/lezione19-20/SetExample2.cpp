#include <iostream>
#include <set>
using namespace std;

int main ()
{
    set<int> c;

    c.insert(1);
    c.insert(2);
    c.insert(4);
    c.insert(5);
    c.insert(6);

    // first element in the container which does not compare less than x
    cout << "lower_bound(3): " << *c.lower_bound(3) << endl;
    
    // first element in the container which compares greater than x
    cout << "upper_bound(3): " << *c.upper_bound(3) << endl;

    // pair: (lower_bound, upper_bound)
    cout << "equal_range(3): " << *c.equal_range(3).first << " "
                               << *c.equal_range(3).second << endl;

    c.insert(3);


    cout << "\nafter c.insert(3)\n";
    cout << "lower_bound(3): " << *c.lower_bound(3) << endl;
    cout << "upper_bound(3): " << *c.upper_bound(3) << endl;
    cout << "equal_range(3): " << *c.equal_range(3).first << " "
                               << *c.equal_range(3).second << endl;

    system("pause");
    return 0;
}
