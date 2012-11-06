/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    string text = "Scrivete a <john@example.com> o <tom@example.com> per informazioni";
    string match = "";
    bool inside = false;

    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];
        if (c == '<') {
            match = "";
            inside = true;
        } else if (c == '>' && inside) {
            cout << match << endl;
            match = "";
            inside = false;
        } else if (inside) {
            match += c;
        }
    }

    return 0;
}
