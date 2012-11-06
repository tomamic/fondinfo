/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef POLYGON_H
#define POLYGON_H

#include "point.h"

#include <vector>
#include <iostream>

using namespace std;

class Polygon
{
public:
    Polygon();
    ~Polygon();

    float perimeter();

    void read(istream& in);
    void write(ostream& out);

private:
    vector<Point*> points;
};

#endif // POLYGON_H
