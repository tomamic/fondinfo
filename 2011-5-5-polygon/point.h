/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef POINT_H
#define POINT_H

#include <iostream>

using namespace std;

class Point
{
public:
    Point();
    Point(float x, float y);

    float getX();
    float getY();
    void setCartesian(float x, float y);

    float getAngle();
    float getRadius();
    void setPolar(float angle, float radius);

    float distance(Point* other);

    void read(istream& in);
    void write(ostream& out);

private:
    float x;
    float y;
};

#endif // POINT_H
