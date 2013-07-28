/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "polygon.h"

using namespace std;

Polygon::Polygon()
{
}

Polygon::~Polygon()
{
    for (int i = 0; i < points.size(); ++i) {
        delete points[i];
    }
}


void Polygon::read(istream& in)
{
    Point* p = new Point();
    p->read(in);
    while (in.good()) {
        points.push_back(p);
        p = new Point();
        p->read(in);
    }
    delete p;
}

void Polygon::write(ostream& out)
{
    for (int i = 0; i < points.size(); ++i) {
        points[i]->write(out);
        out << endl;
    }
}

float Polygon::perimeter()
{
    float result = 0;
    for (int i = 0; i < points.size(); ++i) {
        // the last point is connected to the first one
        int j = (i + 1) % points.size();
        result += points[i]->distance(points[j]);
    }
    return result;
}
