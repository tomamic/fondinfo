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

int mcd1(int m, int n)
{
    clog << "mcd1 " << m << " " << n << endl;
    int result = m;
    if (n != 0) result = mcd1(n, m % n);
    return result;
}

int mcd2(int m, int n)
{
    while (n != 0) {
        clog << "mcd2 " << m << " " << n << endl;
        int r = m % n;
        m = n; n = r;
    }
    clog << "mcd2 " << m << " " << n << endl;
    return m;
}

int main(int argc, char *argv[])
{
    int m = 1071, n = 1029;
    cin >> m >> n;
    cout << mcd1(m, n) << endl;
    cout << mcd2(m, n) << endl;
    return 0;
}
