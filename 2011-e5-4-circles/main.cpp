/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "circle.h"
#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    const int NEW_POINT = 1;
    const int MOVE_POINT = 2;
    const int NEW_CIRCLE = 3;
    const int EXIT = 9;

    vector<Point*> points;
    vector<Circle*> circles;

    int choice;
    do {
        cout << "Points:" << endl;
        for (int i = 0; i < points.size(); ++i) {
            Point* p = points[i];
            cout << setw(2) << i << ". x=" << p->getX() << " y=" << p->getY() << endl;
        }
        cout << "Circles:" << endl;
        for (int i = 0; i < circles.size(); ++i) {
            Circle* c = circles[i];
            Point* p = c->getCenter();
            cout << setw(2) << i << ". x=" << p->getX() << " y=" << p->getY() << " radius=" << c->getRadius() << endl;
        }

        cout << "Enter your coice: " << endl
             << "1. Create point (x, y)" << endl
             << "2. Move point (point-id, x, y)" << endl
             << "3. Create circle (point-id, radius)" << endl
             << "9. Exit" << endl;
        cin >> choice;
        if (choice == NEW_POINT) {
            float x, y;
            cin >> x >> y;
            Point* p = new Point(x, y);
            points.push_back(p);
        } else if (choice == MOVE_POINT) {
            int index; float x, y;
            cin >> index >> x >> y;
            if (0 <= index && index < points.size()) {
                Point* p = points[index];
                p->setCartesian(x, y);
            }
        } else if (choice == NEW_CIRCLE) {
            float index, radius;
            cin >> index >> radius;
            if (0 <= index && index < points.size()) {
                Point* p = points[index];
                Circle* c = new Circle(p, radius);
                circles.push_back(c);
            }
        }
    } while (choice != EXIT);

    for (int i = 0; i < circles.size(); ++ i) {
        delete circles[i];
    }
    circles.clear();
    for (int i = 0; i < points.size(); ++ i) {
        delete points[i];
    }
    points.clear();

    return 0;
}
