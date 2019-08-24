/**
*@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
*@license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/boardgame.hpp"
#include "g2d/boardgamegui.hpp"
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

const vector<vector<int>> dirs = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

class Fifteen : public g2d::BoardGame {
public:
    Fifteen(int w, int h) {
        srand(time(nullptr));
        w_ = w, h_ = h, x0_ = w - 1, y0_ = h - 1;
        auto n = w*h, a1 = pos(w-1, 0), a2 = pos(0, h-1);  // angles
        // start with sorted tiles, then...
        for (auto i = 0; i < n; ++i) {
            board_.push_back((i+1) % n);
        }
        solved_ = board_;
        // do a random walk of the blank tile, until all angle tiles change
        while (board_[0] == 1 || board_[a1] == a1+1 || board_[a2] == a2+1) {
            auto d = dirs[rand() % dirs.size()];
            play_at(x0_+d[0], y0_+d[1]);
        }
    }

    void play_at(int x, int y) {
        auto distance = abs(x - x0_)+abs(y - y0_);
        auto i0 = pos(x0_, y0_), i1 = pos(x, y);
        if (0 <= x && x < w_ && 0 <= y && y < h_ && distance == 1) {
            board_[i0] = board_[i1], board_[i1] = 0;
            x0_ = x, y0_ = y;
        }
    }

    void flag_at(int x, int y) { }
        string value_at(int x, int y) {
        if (0 <= x && x < w_ && 0 <= y && y < h_ && board_[pos(x, y)] > 0) {
            return std::to_string(board_[pos(x, y)]);
        }
        return "";
    }

    bool finished() { return board_ == solved_; }

    string message() { return "Puzzle solved!"; }

    int cols() { return w_; }

    int rows() { return h_; }

private:
    int pos(int x, int y) { return y*w_+x; }

    int w_, h_;
    int x0_, y0_;  // blank
    vector<int> board_, solved_;
};

int main() {
    auto g = new Fifteen{3, 3};
    g2d::gui_play(g);
    // g2d::console_play(g);
}

