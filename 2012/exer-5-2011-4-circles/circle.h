/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
