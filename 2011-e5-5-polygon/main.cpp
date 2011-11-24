/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "polygon.h"
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    cout << "Polygon?" << endl;

    Polygon x;
    x.read(cin); // CTRL+D / CTRL+Z to close the cin stream and terminate input

    cout << x.perimeter() << endl;

    ofstream out("../2011-5-5-polygon/polygon.txt");
    x.write(out);

    return 0;
}
