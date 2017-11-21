/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    const int DELTA = 'a' - 'A';
    const char DASH = '-';

    ifstream file("../2011-2-6-dash/main.cpp");
    file >> noskipws;

    bool dash = false;

    char c;

    file >> c;
    while (file.good()) {

        if ('a' <= c && c <= 'z') {
            cout << char(c - DELTA);
            dash = false;
        } else if (('A' <= c && c <= 'Z') || ('0' <= c && c <= '9')) {
            cout << c;
            dash = false;
        } else if (!dash) {
            cout << DASH;
            dash = true;
        }

        file >> c;
    }

    return 0;
}
