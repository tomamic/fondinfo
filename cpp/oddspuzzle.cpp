#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

class OddsPuzzle {
    int w, h;
    vector<int> matrix;
    vector<bool> annots;
public:
    OddsPuzzle(int cols, int rows) {
        w = cols;
        h = rows;
        auto n = w * h;
        // init matrices
        annots.assign(n, false);
        matrix.assign(n, 0);
        for (auto i = 0; i < n; ++i) {
             matrix[i] = i + 1;
        }
        // shuffle numbers
        for (auto i = 0; i < n; ++i) {
            auto r = rand() % n;
            auto tmp = matrix[i];
            matrix[i] = matrix[r];
            matrix[r] = tmp;
        }
    }

    string value_at(int x, int y) {
        string result;
        if (0 <= x && x < w && 0 <= y && y < h) {
            result = to_string(matrix[y * w + x]);
            if (annots[y * w + x]) {
                result += "!";
            }
        }
        return result;
    }

    void play_at(int x, int y) {
        if (0 <= x && x < w && 0 <= y && y < h) {
            annots[y * w + x] = ! annots[y * w + x];
        }
    }

    bool finished() {
        for (auto i = 0; i < w * h; ++i) {
            auto isodd = matrix[i] % 2 != 0;
            auto annot = annots[i];
            if (isodd != annot) {
                return false;  // incorrect annotation found
            }
        }
        return true;  // no errors found
    }

    void flag_at(int x, int y) { }
    string message() { return "Solved"; }
    int rows() { return h; }
    int cols() { return w; }
};

int main() {
    srand(time(nullptr));
    int w, h;
    cin >> w >> h;

    auto game = OddsPuzzle(w, h);

    for (auto y = 0; y < game.rows(); ++y) {
        for (auto x = 0; x < game.cols(); ++x) {
            cout << game.value_at(x, y);
            if (x < game.cols()-1) {
                cout << ",";
            }
        }
        cout << endl;
    }
}
