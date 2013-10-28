/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char*argv[]) {

    ifstream in("../exer-3-2010-3-scytale/main.cpp");
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
