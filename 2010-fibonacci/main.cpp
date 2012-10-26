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

int fibonacci1(int n)
{
  int result = 1;
  if (n >= 2) {
    clog << "fib " << n << endl;
    result = fibonacci1(n-1) + fibonacci1(n-2);
  }
  return result;
}

int fibonacci2(int n)
{
    static vector<int> lookup(2, 1);

    int result = 1;
    if (n < lookup.size()) {
        result = lookup[n];
    } else {
        clog << "fib " << n << endl;
        result = fibonacci2(n-1) + fibonacci2(n-2);
        lookup.push_back(result);
    }
    return result;
}

int fibonacci3(int n)
{
    int result = 1;
    int fib2 = 1;    // result @ 2 steps before, when n>=2

    for (int i = 2; i <= n; i++) {
        result += fib2;

        // prepare result @ 2 steps before... for next step
        fib2 = result - fib2;
    }

    return result;
}

int main(int argc, char *argv[])
{
    int n; cin >> n;
    while (n > 0) {
        cout << fibonacci1(n) << endl;
        cin >> n;
    }

    return 0;
}
