/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/basic.hpp"
#include "g2d/boardgamegui.hpp"

using namespace g2d;

const std::vector<Point> dirs = { {0, 0}, {0, -1}, {1, 0}, {0, 1}, {-1, 0} };

class LightsOut : public BoardGame {
public:
    LightsOut(int cols, int rows, int level) {
        w_ = cols, h_ = rows;
        board_.assign(h_*w_, false);
        for (auto i = 0; i < level; ++i) {
            play_at(randint(0, w_-1), randint(0, h_-1));
        }
    }

    void play_at(int x, int y) {
        /* Place (or remove) a light at cell (x, y) */
        if (0<=x && x<w_ && 0<=y && y<h_) {
            for (auto d : dirs) {
                auto x1 = x+d.x, y1 = y+d.y;
                if (0<=x1 && x1<w_ && 0<=y1 && y1<h_) {
                    board_[y1*w_+x1] = ! board_[y1*w_+x1];
                }
            }
        }
    }

    std::string value_at(int x, int y) {
        if (0<=x && x<w_ && 0<=y && y<h_ && board_[y*w_+x]) {
            return "@";
        }
        return "-";
    }

    bool finished() {
        for (auto y = 0; y < h_; ++y) {
            for (auto x = 0; x < w_; ++x) {
                if (board_[y*w_+x]) return false;
            }
        }
        return true;
    }

    void flag_at(int x, int y) { }
    int cols() { return w_; }
    int rows() { return h_; }
    std::string message() { return "Solved!"; }

private:
    std::vector<bool> board_;
    int w_, h_;
};

int main() {
    auto g = new LightsOut{5, 5, 4};
    gui_play(g);
    // console_play(g);
}
