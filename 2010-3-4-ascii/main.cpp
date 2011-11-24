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
    const int FIRST = 32;
    const int LAST = 126;
    const int ROWS = 10;
    const int COLS = 10;

    for (int y = 0; y < ROWS; ++y) {
        for (int x = 0; x < COLS; ++x) {
            int i = FIRST + y + x * ROWS;
            //int i = FIRST + y * COLS + x;
            if (i <= LAST) {
                cout << setw(4) << i << ' ' << char(i);
            }
        }
        cout << endl;
    }

    return 0;
}
