/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include "sea.h"

using namespace std;

int main()
{
    srand(time(NULL));
    Sea sea(8, 12);
    int y, x, dir, size;
    while (cin >> size) {
        y = rand() % sea.getRows();
        x = rand() % sea.getCols();
        dir = rand() % sea.getDirs();
        if (!sea.place(y, x, dir, size)) {
            cerr << "ship @ " << y << " " << x << " " << dir << endl;
        }
        sea.print(cout);
    }

    return 0;
}

