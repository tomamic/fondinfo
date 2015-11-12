#include "tictactoe.h"

TicTacToe::TicTacToe(int side) {
    reset(side);
}

void TicTacToe::reset(int side) {
    side_ = side;
    matrix_.assign(side * side, +NONE);
    turn_ = 0;
}

void TicTacToe::play_at(int x, int y) {
    if (get(x, y) == NONE) {
        auto i = x + y * side_;
        if (turn_ % 2 == 0) {
            matrix_[i] = PLR1;
        } else {
            matrix_[i] = PLR2;
        }
        turn_ += 1;
    }
}

char TicTacToe::get(int x, int y) {
    if (0 <= x < side_ && 0 <= y < side_) {
        return matrix_[x + y * side_];
    } else {
        return OUT;
    }
}

// Check a single line, starting at (x, y) and
// advancing for `side` steps in direction (dx, dy).
// If a single player occupies all cells, he's won.
bool TicTacToe::check_line(int x, int y, int dx, int dy) {
    auto player = get(x, y);
    if (player == NONE) return false;
    for (auto i = 1; i < side_; ++i) {
        if (get(x + dx * i, y + dy * i) != player) {
            return false;
        }
    }
    return true;
}

// Check all rows, columns and diagonals.
// Otherwise, check if the game is tied.
char TicTacToe::winner() {
    for (auto x = 0; x < side_; ++x) {
        if (check_line(x, 0, 0, 1)) return get(x, 0);
    }
    for (auto y = 0; y < side_; ++y) {
        if (check_line(0, y, 1, 0)) return get(0, y);
    }
    if (check_line(0, 0, 1, 1)) return get(0, 0);
    if (check_line(side_ - 1, 0, -1, 1)) return get(side_ - 1, 0);
    if (turn_ == side_ * side_) return DRAW;
    return NONE;
}

int TicTacToe::side() {
    return side_;
}

string TicTacToe::str() {
    string out = "";
    for (auto y = 0; y < side_; ++y) {
        for (auto x = 0; x < side_; ++x) {
            out += matrix_[y * side_ + x];
        }
        out += '\n';
    }
    return out;
}
