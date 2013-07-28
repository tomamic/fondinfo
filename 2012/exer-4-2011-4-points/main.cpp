/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>
#include <vector>
#include "point.h"

using namespace std;

int main(int argc, char *argv[])
{
    const int NEW_POINT = 1;
    const int DEL_POINT = 2;
    const int DISTANCE = 3;
    const int EXIT = 9;

    vector<Point*> points;

    int choice;
    do {
        cout << "Points:" << endl;
        for (int i = 0; i < points.size(); ++i) {
            Point* p = points[i];
            cout << i << ": ";
            p->write(cout);
            cout << endl << endl;
        }

        cout << "Enter your coice: " << endl
             << "1. Create point (x, y)" << endl
             << "2. Delete point (index)" << endl
             << "3. Calculate distance (index1, index2)" << endl
             << "9. Exit" << endl << endl;
        cin >> choice;
        if (choice == NEW_POINT) {
            Point* p = new Point();
            p->read(cin);
            points.push_back(p);
        } else if (choice == DEL_POINT) {
            int id;
            cin >> id;
            if (0 <= id && id < points.size()) {
                Point* p = points[id];
                delete p;
                points.erase(points.begin() + id);
            }
        } else if (choice == DISTANCE) {
            int id1, id2;
            cin >> id1 >> id2;
            if (0 <= id1 && id1 < points.size()
                    && 0 <= id2 && id2 < points.size()) {
                Point* p1 = points[id1];
                Point* p2 = points[id2];
                cout << p1->distance(p2) << endl;
            }
        }
    } while (choice != EXIT);

//    for (int i = 0; i < points.size(); ++i) {
//        delete points[i];
//    }
//    points.clear();

    return 0;
}
