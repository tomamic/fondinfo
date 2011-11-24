/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    const string END = "end";
    int count = 0;
    int length = 0;

    string word;
    cin >> word;
    while (word != END) {
        ++count;
        length += word.size();
        cin >> word;
    }

    if (count != 0) {
        cout << (length / count) << endl;
    }

    return 0;
}
