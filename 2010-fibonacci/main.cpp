/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <vector>

using namespace std;

int fibonacci(int n)
{
    static vector<int> lookup(2, 1);

    int result = 1;
    if (n > 1) {
        if (n < lookup.size()) result = lookup[n];
        else {
            clog << "fib " << n << endl;
            result = fibonacci(n-1) + fibonacci(n-2);
            lookup.push_back(result);
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int n; cin >> n;
    while (n > 0) {
        cout << fibonacci(n) << endl;
        cin >> n;
    }

    return 0;
}
