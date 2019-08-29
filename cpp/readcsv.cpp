/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ofstream file0{"matrix.csv"};
    file0 << "5,7,2,11\n1,3,12,9\n4,6,10,8";
    file0.close();

    ifstream file1{"matrix.csv"};
    vector<int> matrix;
    auto cols = 0, rows = 0;

    for (string line; getline(file1, line);) {
        istringstream sstr{line};
        for (string item; getline(sstr, item, ',');) {
            matrix.push_back(stoi(item));
        }

        if (cols == 0) { cols = matrix.size(); }
        ++rows;
    }

    file1.close();
    cout << cols << ' ' << rows << endl;

    auto total = 0, x = cols-1, y = rows-1;
    while (x >= 0 && y >= 0) {
        total += matrix[y * cols + x];
        --x; --y;
    }
    cout << total << endl;
}

