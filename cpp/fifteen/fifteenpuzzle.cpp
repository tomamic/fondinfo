/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteenpuzzle.h"

#include <cstdlib>
#include <sstream>
#include <iomanip>
#include <stdexcept>

using namespace std;

FifteenPuzzle::FifteenPuzzle(int cols, int rows) {
    if (cols < 2 || rows < 2)
        throw invalid_argument("too small puzzle");
    init(cols, rows);
    shuffle();
}

void FifteenPuzzle::init(int cols, int rows) {
    // allocate the matrix
    this->cols_ = cols;
    this->rows_ = rows;
    board_.assign(cols * rows, +BLANK);
    // put ordered values in each cell
    for (auto i = 0; i < board_.size() - 1; ++i) {
        board_[i] = FIRST + i;
    }
    // put the blank value in the last cell
    board_[board_.size() - 1] = BLANK;
    blank_ = {cols_ - 1, rows_ - 1};
    moved_ = blank_;
}

void FifteenPuzzle::shuffle() {
    do {
        // random walk: move the blank cell repeatedly
        auto walk_length = rows_ * rows_ * cols_ * cols_;
        for (auto i = 0; i < walk_length; ++i) {
            // choose randomly one of the 4 neighbors
            auto dir = DIRS[rand() % DIRS.size()];
            auto neighbor = blank_ + dir;
            if (is_inside(neighbor)) {
                swap_blank_with(neighbor);
            }
        }
    } while (is_finished());
}

void FifteenPuzzle::move(int value) {
    // for each neighbor of blank (4 directions)...
    for (auto dir : DIRS) {
        auto neighbor = blank_ + dir;
        if (is_inside(neighbor) && get(neighbor) == value) {
            swap_blank_with(neighbor);
            return;
        }
    }
}

void FifteenPuzzle::move(Coord cell) {
    // get the value of cell, move that value
    move(get(cell));
}

bool  FifteenPuzzle::is_inside(Coord cell) const {
    auto x = cell.real(), y = cell.imag();
    return 0 <= x && x < cols_ && 0 <= y && y < rows_;
}

int FifteenPuzzle::get(Coord cell) const
{
    if (!is_inside(cell))
        throw invalid_argument("out of bounds");
    auto x = cell.real(), y = cell.imag();
    return board_[y * cols_ + x];
}

void FifteenPuzzle::set(Coord cell, int value)
{
    auto x = cell.real(), y = cell.imag();
    board_[y * cols_ + x] = value;
}

void FifteenPuzzle::swap_blank_with(Coord cell)
{
    moved_ = blank_;
    blank_ = cell;
    set(moved_, get(blank_));
    set(blank_, BLANK);
}

bool FifteenPuzzle::is_finished() const
{
    for (auto i = 0; i < board_.size() - 1; ++i) {
        // a cell with wrong value? puzzle not solved!
        if (board_[i] != FIRST + i) return false;
    }
    return true;
}

string FifteenPuzzle::str() const
{
    ostringstream out;
    for (auto i = 0; i < board_.size(); ++i) {
        out << setw(3) << board_[i];
        if (i % cols_ == cols_ - 1) out << endl;
    }
    return out.str();
}
