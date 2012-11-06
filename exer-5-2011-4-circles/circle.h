/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef CIRCLE_H
#define CIRCLE_H

#include "point.h"

#include <vector>
#include <iostream>

using namespace std;

class Circle
{
public:
    Circle(Point* center, float radius);
    ~Circle();
    Point* getCenter();
    float getRadius();

    float perimeter();
    float area();

private:
    Point* center;
    float radius;
};

#endif // CIRCLE_H
