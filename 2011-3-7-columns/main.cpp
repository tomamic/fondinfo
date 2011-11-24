/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
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
    const int FIRST = -15;
    const int COLS = 5;
    const int ROWS = 12;

    for (int y = 0; y < ROWS; ++y) {
        for (int x = 0; x < COLS; ++x) {
            int cent = y + x * ROWS + FIRST;
            float fahr = 32 + 1.8 * cent;
            cout << setw(4) << cent << setw(8) << fixed << setprecision(2) << fahr << " |";
        }
        cout << endl;
    }

    return 0;
}
