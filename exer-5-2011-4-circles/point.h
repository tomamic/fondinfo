/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
