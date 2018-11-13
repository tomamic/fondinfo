#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> split(string text, char sep) {
    vector<int> values;

    istringstream sstr{text};
    string item;
    while (getline(sstr, item, sep)) {
        values.push_back(stoi(item));
    }
    return values;
}

int main() {
    ofstream file0{"matrix.csv"};
    file0 << "5,7,2,11\n1,3,12,9\n4,6,10,8";
    file0.close();

    ifstream file1{"matrix.csv"};

    auto cols = 0, rows = 0;

    vector<int> matrix1;
//    vector<vector<int>> matrix2;

    for (string line; getline(file1, line);) {
        auto values = split(line, ',');
        if (cols == 0) {
            cols = values.size();
        }

        for (auto v : values) {
            matrix1.push_back(v);
        }
//        matrix2.push_back(values);
        ++rows;
    }
    file1.close();

    cout << cols << ' ' << rows << endl;

    auto total = 0;
    auto x = cols -1, y = rows - 1;
    while (x >= 0 && y >= 0) {
        total += matrix1[y * cols + x];
//        total += matrix2[y][x];
        --x; --y;
    }
    cout << total << endl;
}

