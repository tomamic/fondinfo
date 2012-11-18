/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
    int fib2 = 1;    // result @ 2 steps before

    for (int i = 2; i <= n; i++) {
        result += fib2;

        // store previous result, for next step
        fib2 = result - fib2;
    }

    return result;
}

int main(int argc, char *argv[])
{
    int n;
    while (cin >> n) {
        cout << fibonacci1(n) << endl;
    }

    return 0;
}
