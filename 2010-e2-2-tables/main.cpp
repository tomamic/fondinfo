/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    int x, y;

    for (y = 1; y <= 10; ++y) {

        for (x = 1; x <= 10; ++x) {
            cout << setw(4) << x * y;
        }
        cout << endl;

    }

    return 0;
}
