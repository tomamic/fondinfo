/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "board.h"

#include <iostream>
#include <sstream>

int main(int argc, char *argv[])
{
    int side;
    cin >> side;

    Board b(side, side);
    b.solve();
    b.write(cout);
    return 0;
}
