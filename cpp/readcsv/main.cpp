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
    ifstream file1{"../readcsv/matrix.csv"};

    auto cols = 0, rows = 0;

    vector<int> matrix;

    string line;
    while (getline(file1, line)) {
        auto values = split(line, ',');
        if (cols == 0) cols = values.size();
        for (auto v : values) {
            matrix.push_back(v);
        }
        ++rows;
    }
    file1.close();

    cout << cols << ' ' << rows << endl;

    auto total = 0;
    auto x = cols -1, y = rows - 1;
    while (x >= 0 && y >= 0) {
        total += matrix[y * cols + x];
        --x; --y;
    }
    cout << total << endl;
}

