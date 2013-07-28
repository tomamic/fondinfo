/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
