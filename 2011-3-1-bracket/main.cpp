/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream file("../2011-3-1-bracket/main.cpp");
    file >> noskipws;

    bool inside = false;

    char c;
    file >> c;
    while (file.good()) {

        if (c == '(') {
            inside = true;
        } else if (c == ')' && inside) {
            inside = false;
        } else if (!inside) {
            cout << c;
        }

        file >> c;
    }

    return 0;
}
