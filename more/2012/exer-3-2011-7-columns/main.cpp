/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    const int FIRST = -15;
    const int COLS = 5;
    const int ROWS = 12;

    for (int y = 0; y < ROWS; ++y) {
        for (int x = 0; x < COLS; ++x) {
            int cent = y + x * ROWS + FIRST;
            float fahr = 32 + 1.8 * cent;
            cout << setw(4) << cent << setw(8) << fixed << setprecision(2) << fahr << " |";
        }
        cout << endl;
    }

    return 0;
}
