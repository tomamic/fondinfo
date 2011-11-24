/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int x, cube;

    do {
        cin >> x;

        if (x != 0) {
            cube = x * x * x;
            cout << cube << endl;
        }

    } while (x != 0);


    return 0;
}
