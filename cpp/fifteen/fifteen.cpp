/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteen.h"
#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

const vector<vector<int>> dirs = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

Fifteen::Fifteen(int w, int h) {
    srand(time(nullptr));
    w_ = w, h_ = h, x0_ = w - 1, y0_ = h - 1;
    auto n = w * h, a1 = pos(w - 1, 0), a2 = pos(0, h - 1);  // angles
    // start with sorted tiles, then...
    for (auto i = 0; i < n; ++i) {
        board_.push_back((i + 1) % n);
    }
    solved_ = board_;
    // do a random walk of the blank tile, until all angle tiles change
    while (board_[0] == 1 || board_[a1] == a1+1 || board_[a2] == a2+1) {
        auto d = dirs[rand() % dirs.size()];
        play_at(x0_+d[0], y0_+d[1]);
    }
}

void Fifteen::play_at(int x, int y) {
    auto dist = abs(x-x0_) + abs(y-y0_), i0 = pos(x0_, y0_), i1 = pos(x, y);
    if (0 <= x && x < w_ && 0 <= y && y < h_ && dist == 1) {
        board_[i0] = board_[i1], board_[i1] = 0;
        x0_ = x, y0_ = y;
    }
}

string Fifteen::get_val(int x, int y) {
    if (0 <= x && x < w_ && 0 <= y && y < h_ && board_[pos(x, y)] > 0) {
        return to_string(board_[pos(x, y)]);
    }
    return "";
}
