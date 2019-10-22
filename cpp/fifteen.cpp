/**
*@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
*@license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/basic.hpp"
//#include "g2d/boardgamegui.hpp"

using namespace g2d;

const std::vector<Point> dirs = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

class Fifteen : public BoardGame {
public:
    Fifteen(int cols, int rows) {
        w_ = cols, h_ = rows, x0_ = w_ - 1, y0_ = h_ - 1;
        auto n = w_*h_;
        // start with sorted tiles, then...
        for (auto i = 0; i < n; ++i) {
            board_.push_back((i+1) % n);
        }
        solved_ = board_;
        // do a random walk of the blank tile
        while (board_.back() != 1) {
            auto d = dirs[randint(0, dirs.size()-1)];
            play_at(x0_+d.x, y0_+d.y);
        }
    }

    std::string value_at(int x, int y) {
        if (0 <= x && x < w_ && 0 <= y && y < h_ && board_[y*w_+x] > 0) {
            return std::to_string(board_[y*w_+x]);
        }
        return "";
    }

    void play_at(int x, int y) {
        auto distance = abs(x - x0_) + abs(y - y0_);
        if (0 <= x && x < w_ && 0 <= y && y < h_ && distance == 1) {
            board_[y0_*w_+x0_] = board_[y*w_+x];
            board_[y*w_+x] = 0;
            x0_ = x; y0_ = y;
        }
    }

    void flag_at(int x, int y) { }
    bool finished() { return board_ == solved_; }
    std::string message() { return "Puzzle solved!"; }
    int cols() { return w_; }
    int rows() { return h_; }

private:
    int w_, h_;
    int x0_, y0_;  // blank
    std::vector<int> board_, solved_;
};

int main() {
    auto g = new Fifteen{3, 3};
    //gui_play(g);
    console_play(g);
}

