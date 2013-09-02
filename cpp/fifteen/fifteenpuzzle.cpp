/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteenpuzzle.h"

#include <cstdlib>
#include <sstream>

using namespace std;

FifteenPuzzle::FifteenPuzzle(int cols, int rows)
{
    if (cols < 2) { cols = 2; }
    if (rows < 2) { rows = 2; }
    this->cols_ = cols;
    this->rows_ = rows;
    board_.assign(cols * rows, +BLANK);
    sort();
    shuffle();
}

void FifteenPuzzle::sort()
{
    // put ordered symbols in each cell
    for (auto i = 0; i < board_.size(); ++i) {
        board_[i] = FIRST + i;
    }
    // put blank in the last cell
    blank_ = {cols_ - 1, rows_ - 1};
    set({blank_}, BLANK);
    moved_ = blank_;
}

void FifteenPuzzle::shuffle()
{
    do {
        // perform a random walk (SIZE^2 steps) of the blank cell
        auto walk_length = rows_ * rows_ * cols_ * cols_;
        for (auto i = 0; i < walk_length; ++i) {
            auto dir = DIRS[rand() % DIRS.size()];
            // consider the cell adjacent to the
            // blank cell, in the current direction
            auto next = blank_ + dir;
            // if it is inside the board, then move the blank
            if (get(next) != OUT_OF_BOUNDS) {
                moveBlank(dir);
            }
        }
    } while (finished());
}

void FifteenPuzzle::move(char symbol)
{
    // for each direction, while symbol not yet found...
    for (auto dir : DIRS) {
        // consider the cell next to the blank cell
        auto next = blank_ + dir;
        // if the symbol to move is here...
        if (get(next) == symbol) {
            // move blank this way!
            moveBlank(dir);
            return;
        }
    }
}

void FifteenPuzzle::move(Coord pos)
{
    auto symbol = get(pos);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(Coord pos) const
{
    auto x = pos.real(), y = pos.imag();
    auto value = OUT_OF_BOUNDS;
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        value = board_[y * cols_ + x];
    }
    return value;
}

void FifteenPuzzle::set(Coord pos, char value)
{
    auto x = pos.real(), y = pos.imag();
    board_[y * cols_ + x] = value;
}

void FifteenPuzzle::moveBlank(Coord dir)
{
    moved_ = blank_;
    blank_ += dir;
    set(moved_, get(blank_));
    set(blank_, BLANK);
}

bool FifteenPuzzle::finished() const
{
    for (auto i = 0; i < board_.size() - 1; ++i) {
        // if the cell has the wrong symbol...
        // puzzle is not yet solved!
        if (board_[i] != FIRST + i) return false;
    }
    return true;
}

string FifteenPuzzle::str() const
{
    ostringstream out;
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            out << get({x, y});
        }
        out << endl;
    }
    out << endl;
    return out.str();
}
