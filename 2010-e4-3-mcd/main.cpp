/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

using namespace std;

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

int mcd(int m, int n) {
    if (m > n) swap(m, n);
    clog << "mcd(" << m << ", " << n << ")" << endl;

    int result = n;
    if (m != 0) result = mcd(m, n % m);
    return result;
}

int mcd2(int m, int n) {
    do {
        if (m > n) swap(m, n);
        clog << "mcd2(" << m << ", " << n << ")" << endl;

        if (m != 0)  n = n % m;
    } while (m > 0);
    return n;
}

int main(int argc, char *argv[])
{
    int m = 72, n = 96;
    cin >> m >> n;
    cout << mcd(m, n) << endl;
    cout << mcd2(m, n) << endl;

    return 0;
}
