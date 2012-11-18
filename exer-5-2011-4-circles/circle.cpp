/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
