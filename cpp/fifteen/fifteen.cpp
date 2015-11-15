/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteen.h"

#include <cstdlib>
#include <sstream>
#include <iomanip>

using namespace std;

Fifteen::Fifteen(int cols, int rows) {
    init(cols, rows);
}

void Fifteen::init(int cols, int rows) {
    // allocate the matrix
    this->cols_ = cols;
    this->rows_ = rows;
    board_.assign(cols * rows, 0);
    // put ordered values in each cell
    for (auto i = 0; i < board_.size() - 1; ++i) {
        board_[i] = i + 1;
    }
    blank_ = {cols_ - 1, rows_ - 1};
    moved_ = blank_;
    new_game();
}

void Fifteen::new_game() {
    // random walk: move the blank cell repeatedly
    auto walk_length = rows_ * rows_ * cols_ * cols_;
    for (auto i = 0; i < walk_length; ++i) {
        // choose randomly one of the 4 neighbors
        auto dir = DIRS[rand() % DIRS.size()];
        auto neighbor = blank_ + dir;
        auto x = neighbor.real(), y = neighbor.imag();
        swap_blank_with(x, y);
    }
    // may happen, with small boards...
    if (finished()) new_game();
}

void Fifteen::move_val(int value) {
    if (value < 1 || value >= board_.size()) return;
    // Search around the blank cell,
    // if val is found in a cell,
    // then swap it with the blank cell'''
    for (auto dir : DIRS) {
        auto neighbor = blank_ + dir;
        auto x = neighbor.real(), y = neighbor.imag();
        if (get(x, y) == value) {
            swap_blank_with(x, y);
            return;
        }
    }
}

void Fifteen::play_at(int x, int y) {
    // get the value of cell, move that value
    move_val(get(x, y));
}

string Fifteen::get_val(int x, int y) const {
    int val = get(x, y);
    if (val <= 0) return "";
    return to_string(val);
}

int Fifteen::get(int x, int y) const {
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        return board_[y * cols_ + x];
    }
    return -1;
}

void Fifteen::swap_blank_with(int x, int y) {
    auto x0 = blank_.real(), y0 = blank_.imag();
    auto val = get(x, y);
    if (val > 0) {
        board_[y0 * cols_ + x0] = val;
        board_[y * cols_ + x] = 0;
        moved_ = blank_;
        blank_ = {x, y};
    }
}

bool Fifteen::finished() const {
    for (auto i = 0; i < board_.size() - 1; ++i) {
        // a cell with wrong value? puzzle not solved!
        if (board_[i] != i + 1) return false;
    }
    return true;
}

string Fifteen::str() const {
    ostringstream out;
    for (auto i = 0; i < board_.size(); ++i) {
        out << setw(3) << board_[i];
        if (i % cols_ == cols_ - 1) out << endl;
    }
    return out.str();
}
