/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/actor.hpp"
#include "g2d/boardgame.hpp"
#include "g2d/boardgamegui.hpp"

using std::string;
using std::vector;

const vector<g2d::Point> dirs = { {0, 0}, {0, -1}, {1, 0}, {0, 1}, {-1, 0} };

class LightsOut : public g2d::BoardGame {
public:
    LightsOut(int level, int cols, int rows) {
        cols_ = cols, rows_ = rows;
        board_.assign(rows*cols, false);
        for (auto i = 0; i < level; ++i) {
            play_at(g2d::randint(0, cols-1), g2d::randint(0, rows-1));
        }
    }

    void play_at(int x, int y) {
        /* Place (or remove) a light at cell (x, y) */
        if (0<=x && x<cols_ && 0<=y && y<rows_) {
            for (auto d : dirs) {
                auto x1 = x+d.x, y1 = y+d.y;
                if (0<=x1 && x1<cols_ && 0<=y1 && y1<rows_) {
                    board_[y1*cols_+x1] = ! board_[y1*cols_+x1];
                }
            }
        }
    }

    string value_at(int x, int y) {
        if (0<=x && x<cols_ && 0<=y && y<rows_ && board_[y*cols_+x]) {
            return "@";
        }
        return "-";
    }

    bool finished() {
        for (auto y = 0; y < rows_; ++y) {
            for (auto x = 0; x < cols_; ++x) {
                if (board_[y*cols_+x]) return false;
            }
        }
        return true;
    }

    void flag_at(int x, int y) { }

    int cols() { return rows_; }

    int rows() { return cols_; }

    string message() { return "Solved!"; }

private:
    vector<bool> board_;
    int cols_;
    int rows_;
};

int main() {
    auto g = new LightsOut{4, 5, 5};
    g2d::gui_play(g);
    // g2d::console_play(g);
}
