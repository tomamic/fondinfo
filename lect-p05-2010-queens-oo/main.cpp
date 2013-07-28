/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "board.h"

#include <iostream>
#include <sstream>

int main(int argc, char *argv[])
{
    int side;
    cout << "side? ";
    cin >> side;

    Board b(side);
    b.solve();
    b.write(cout);

    return 0;
}
