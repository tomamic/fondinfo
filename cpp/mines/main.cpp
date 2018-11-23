#include <iostream>
#include <vector>
#include <iomanip>  /* for setw */

using namespace std;

int main() {
    srand(time(nullptr));

    auto w = 6, h = 4, n = 10;  // todo: ask the user, check

    // 1. these would go in a class definition...
    vector<int> matrix;
    int MINE = 9;
    vector<vector<int>> dirs = {  // list of pairs (dx, dy)
        {0, -1}, {1, -1}, {1, 0}, {1, 1},
        {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}};

    // 2. ... and these in the method definitions
    // create and fill the matrix
    matrix.assign(w * h, 0);
    for (auto i = 0; i < n; ++i) {
        auto x = rand() % w, y = rand() % h;
        matrix[y * w + x] = MINE;  // todo: count only if empty
    }

    // show the matrix
    for (auto y = 0; y < h; ++y) {
        for (auto x = 0; x < w; ++x) {
            cout << setw(2) << matrix[y * w + x];
        }
        cout << endl;
    }

    // count mines around (x, y)
    auto x = 4, y = 2, mines = 0;  // todo: ask the user, check
    for (auto d : dirs) {
        auto x1 = x + d[0], y1 = y + d[1];
        if (0 <= x1 && x1 < w && 0 <= y1 && y1 < h &&
                matrix[y1 * w + x1] == MINE) {
            ++mines;
        }
    }
    cout << mines << endl;
}
