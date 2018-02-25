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
    for (auto i = 0; i < board_.size() - 1; ++i) {
        board_[i] = i + 1;
    }
    solution_ = board_;
    blx_ = cols_ - 1, bly_ = rows_ - 1;

    // random walk: move the blank cell repeatedly
    auto walk_length = rows_ * rows_ * cols_ * cols_;
    for (auto i = 0; i < walk_length || finished(); ++i) {
        // choose randomly one of the 4 neighbors
        const vector<vector<int>> dirs = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
        auto dir = dirs[rand() % dirs.size()];
        play_at(blx_ + dir[0], bly_ + dir[1]);
    }
}

void Fifteen::play_at(int x, int y) {
    if (0 <= x && x < cols_ && 0 <= y && y < rows_ &&
            abs(blx_ - x) + abs(bly_ - y) == 1) {
        board_[bly_ * cols_ + blx_] = board_[y * cols_ + x];
        board_[y * cols_ + x] = 0;
        blx_ = x, bly_ = y;
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

