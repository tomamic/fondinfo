#include "queens.h"

vector<vector<int>> dirs = { {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0} };

Queens::Queens(int side)
{
    side_ = side;
    queens_ = side;
    board_.assign(side, vector<int>(side, 0));
    cover_.assign(side, vector<int>(side, 0));
}

void Queens::play_at(int x, int y)
{
    if (0 <= x && x < side_ && 0 <= y && y < side_) {
        auto val = 1;
        if (board_[y][x] != 0) val = -1;

        queens_ -= val;
        board_[y][x] += val;
        //cover_[y][x] += val;

        for (auto d : dirs) {
            auto mx = x + d[0], my = y + d[1];
            while (0 <= mx && mx < side_ && 0 <= my && my < side_) {
                cover_[my][mx] += val;
                mx += d[0]; my += d[1];
            }
        }
    }
}

string Queens::get_val(int x, int y)
{
    if (0 <= x && x < side_ && 0 <= y && y < side_) {
        //return to_string(board_[y][x]) + to_string(cover_[y][x]);
        if (board_[y][x] != 0) return "@";
        if (cover_[y][x] != 0) return "+";
    }
    return " ";
}

bool Queens::finished()
{
    if (queens_ != 0) return false;
    for (int y = 0; y < side_; ++y) {
        for (int x = 0; x < side_; ++x) {
            if (board_[y][x] != 0 && cover_[y][x] != 0) {
                return false;
            }
        }
    }
    return true;
}
