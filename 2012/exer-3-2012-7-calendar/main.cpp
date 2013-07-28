/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    const int WEEK_DAYS = 7;
    const int MAX_WEEKS = 6;

    int first;
    cout << "first (0-6)? ";
    cin >> first;

    int length;
    cout << "length (28-31)? ";
    cin >> length;

    for (int i = 0; i < WEEK_DAYS * MAX_WEEKS; ++i) {
        int day = i + 1 - first;
        if (0 < day && day <= length) {
            cout << setw(3) << day;
        } else {
            cout << "   ";
        }
        if (i % WEEK_DAYS == WEEK_DAYS - 1) {
            cout << endl;
        }
    }

    cout << endl;

    for (int y = 0; y < MAX_WEEKS; ++y) {
        for (int x = 0; x < WEEK_DAYS; ++x) {
            int day = y * WEEK_DAYS + x + 1 - first;
            if (0 < day && day <= length) {
                cout << setw(3) << day;
            } else {
                cout << "   ";
            }
        }
        cout << endl;
    }

    cout << endl;

    for (int y = 0; y < WEEK_DAYS; ++y) {
        for (int x = 0; x < MAX_WEEKS; ++x) {
            int day = y + x * WEEK_DAYS + 1 - first;
            if (0 < day && day <= length) {
                cout << setw(3) << day;
            } else {
                cout << "   ";
            }
        }
        cout << endl;
    }
    
    return 0;
}
