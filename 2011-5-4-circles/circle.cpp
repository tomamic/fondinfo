/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "circle.h"
#include <cmath>

using namespace std;

Circle::Circle(Point* center, float radius) :
    center(center),
    radius(radius)
{
}

Circle::~Circle()
{
}

Point* Circle::getCenter()
{
    return center;
}

float Circle::getRadius()
{
    return radius;
}

float Circle::perimeter()
{
    return 2 * M_PI * radius;
}

float Circle::area() {
    return M_PI * radius * radius;
}
