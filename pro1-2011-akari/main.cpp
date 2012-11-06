/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <fstream>
#include "akaripuzzle.h"

int main(int argc, char *argv[])
{
    AkariPuzzle puzzle;
    ifstream in("../2011-p1-akari/game.txt");
    puzzle.read(in);
    puzzle.write(cout);

    int y, x;
    cin >> y >> x;
    while (cin.good()) {
        puzzle.putBulb(y, x);
        puzzle.write(cout);
        cin >> y >> x;
    }

    return 0;
}
