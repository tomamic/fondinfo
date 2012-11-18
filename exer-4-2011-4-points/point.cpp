/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "point.h"
#include <cmath>

using namespace std;

Point::Point() :
    x(0), y(0)
{
}

Point::Point(float x, float y) :
    x(x), y(y)
{
//    this->x = x;
//    this->y = y;
}

float Point::getX()
{
    return x;
}

float Point::getY()
{
    return y;
}

void Point::setCartesian(float x, float y)
{
    this->x = x;
    this->y = y;
}

float Point::getAngle()
{
    return atan2(y, x) * 180.0 / M_PI;
}

float Point::getRadius()
{
    return sqrt(x * x + y * y);
}

void Point::setPolar(float angle, float radius)
{
    x = radius * cos(angle * M_PI / 180.0);
    y = radius * sin(angle * M_PI / 180.0);
}

void Point::read(istream& in) {
    in >> x >> y;
}

void Point::write(ostream& out) {
    out << x << ' ' << y;
}

float Point::distance(Point* other) {
    float dx = x - other->x;
    float dy = y - other->y;
    return sqrt(dx * dx + dy * dy);
}
