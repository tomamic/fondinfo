/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char*argv[]) {

    ifstream in("../2010-e3-3-scytale/main.cpp");
    ofstream out("out.txt");
    in >> noskipws;

    const char FILLER = ' ';
    const int ROWS = 3;
    const int COLS = 4;
    vector<vector<char> > matrix(ROWS, vector<char>(COLS));

    while (in.good()) {
        for (int y = 0; y < ROWS; ++y) {
            for (int x = 0; x < COLS; ++x) {
                char c = FILLER;
                in >> c; // is "in" still good?
                matrix[y][x] = c;
            }
        }

        for (int x = 0; x < COLS; ++x) {
            for (int y = 0; y < ROWS; ++y) {
                out << matrix[y][x];
            }
        }
    }

    return 0;
}
