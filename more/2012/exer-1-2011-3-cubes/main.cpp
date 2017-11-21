/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int x, cube;

    do {
        cin >> x;

        if (x != 0) {
            cube = x * x * x;
            cout << cube << endl;
        }

    } while (x != 0);


    return 0;
}
