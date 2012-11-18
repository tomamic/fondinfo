/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    const int FIRST = 32;
    const int LAST = 126;
    const int ROWS = 10;
    const int COLS = 10;

    for (int y = 0; y < ROWS; ++y) {
        for (int x = 0; x < COLS; ++x) {
            int i = FIRST + y + x * ROWS;
            //int i = FIRST + y * COLS + x;
            if (i <= LAST) {
                cout << setw(4) << i << ' ' << char(i);
            }
        }
        cout << endl;
    }

    return 0;
}
