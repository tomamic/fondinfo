/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteen.h"

#include <cstdlib>
#include <ctime>

using namespace std;

Fifteen::Fifteen(int cols, int rows) {
    srand(time(nullptr));
    // allocate the matrix
    cols_ = cols, rows_ = rows;
    board_.assign(cols * rows, 0);
    // put ordered values in each cell
    for (auto i = 0; i < cols * rows - 1; ++i) {
        board_[i] = i + 1;
    }
    solution_ = board_;
    x0_ = cols_ - 1, y0_ = rows_ - 1;

    // random walk: move the blank cell repeatedly
    auto walk_length = rows_ * rows_ * cols_ * cols_;
    for (auto i = 0; i < walk_length || finished(); ++i) {
        // choose randomly one of the 4 neighbors
        const vector<vector<int>> dirs = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
        auto dir = dirs[rand() % dirs.size()];
        play_at(x0_ + dir[0], y0_ + dir[1]);
    }
}

void Fifteen::play_at(int x, int y) {
    if (0 <= x && x < cols_ && 0 <= y && y < rows_ &&
            abs(x - x0_) + abs(y - y0_) == 1) {
        board_[y0_ * cols_ + x0_] = board_[y * cols_ + x];
        board_[y * cols_ + x] = 0;
        x0_ = x, y0_ = y;
    }
}

string Fifteen::get_val(int x, int y) {
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        auto val = board_[y * cols_ + x];
        if (val > 0) {
            return to_string(val);
        }
    }
    return "";
}

