/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include "memory.h"
#include <cstdlib>
#include <ctime>

int main(int argc, char *argv[])
{
    srand(time(NULL));

    int rows = 1, cols = 1, size = 1;
    while (size % 2 != 0) {
        cout << "Rows and cols?" << endl;
        cin >> rows >> cols;
        size = rows * cols;
    }

    Memory memory(rows, cols);
    memory.write(cout);

    int a, b;
    cout << "Two cards (1-" << size << ")?" << endl;
    cin >> a >> b;
    while (cin.good() && !memory.isSolved()) {
        memory.move(a - 1, b - 1);
        memory.write(cout);

        if (!memory.isSolved()) {
            cout << "Two cards (1-" << size << ")?" << endl;
            cin >> a >> b;
        }
    }

    return 0;
}
