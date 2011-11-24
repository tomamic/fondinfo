/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    string text = "Hey!! It's 2010, yet";

    bool dash = false;
    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];
        if ('A' <= c && c <= 'Z') {
            c += 'a' - 'A';
            dash = false;
            cout << c;
        } else if (('0' <= c && c <= '9')
            || ('a' <= c && c <= 'z')) {
            dash = false;
            cout << c;
        } else if (!dash) {
            dash = true;
            cout << '-';
        }
    }
    cout << endl;

    return 0;
}
