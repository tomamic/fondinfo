#ifndef LIGHTSOUT_H
#define LIGHTSOUT_H

#include "boardgame.hpp"
#include <cstdlib>
#include <ctime>
#include <vector>

using std::string;
using std::vector;

class LightsOut : public BoardGame
{
public:
    LightsOut(int level, int cols, int rows);
    void play_at(int x, int y);
    void flag_at(int x, int y) { }
    string value_at(int x, int y);
    bool finished();
    int cols() { return rows_; }
    int rows() { return cols_; }
    string message() { return "Solved!"; }
private:
    vector<vector<bool>> board_;
    int cols_;
    int rows_;
};


LightsOut::LightsOut(int level, int cols, int rows)
{
    srand(time(nullptr));
    cols_ = cols, rows_ = rows;
    board_.assign(rows, vector<bool>(cols, false));
    for (auto i = 0; i < level; ++i) {
        play_at(rand() % cols, rand() % rows);
    }
}

void LightsOut::play_at(int x, int y)
{
    /* Place (or remove) a light at cell (x, y) */
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        vector<vector<int>> dirs = { {0, 0}, {0, -1}, {1, 0}, {0, 1}, {-1, 0} };
        for (auto d : dirs) {
            auto x1 = x + d[0], y1 = y + d[1];
            if (0 <= x1 && x1 < cols_ && 0 <= y1 && y1 < rows_) {
                board_[y1][x1] = ! board_[y1][x1];
            }
        }
    }
}

string LightsOut::value_at(int x, int y)
{
    if (0 <= x && x < cols_ && 0 <= y && y < rows_ && board_[y][x]) {
        return "@";
    }
    return "-";
}

bool LightsOut::finished()
{
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            if (board_[y][x]) return false;
        }
    }
    return true;
}

#endif // LIGHTSOUT_H
