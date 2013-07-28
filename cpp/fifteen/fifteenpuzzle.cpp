/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteenpuzzle.h"

#include <cstdlib>
#include <sstream>

using namespace std;

// DIRS is a vector of couples: (dx, dy)
const vector<vector<int>> DIRS{{0, -1}, {-1, 0}, {0, 1}, {1, 0}};

FifteenPuzzle::FifteenPuzzle(int cols, int rows)
{
    if (cols < 2) { cols = 2; }
    if (rows < 2) { rows = 2; }
    this->cols_ = cols;
    this->rows_ = rows;
    board.assign(cols * rows, +BLANK_SYMBOL);
    sort();
    shuffle();
}

int FifteenPuzzle::cols() const
{
    return cols_;
}

int FifteenPuzzle::rows() const
{
    return rows_;
}

void FifteenPuzzle::sort()
{
    // put ordered symbols in each cell (ltr, ttb)
    auto value = FIRST_SYMBOL;
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            set(x, y, value);
            ++value;
        }
    }
    // put blank in the last cell
    blankX = cols_ - 1;
    blankY = rows_ - 1;
    set(blankX, blankY, BLANK_SYMBOL);
}

void FifteenPuzzle::shuffle()
{
    do {
        // perform a random walk (SIZE^2 steps) of the blank cell
        auto walk_length = rows_ * rows_ * cols_ * cols_;
        for (auto i = 0; i < walk_length; ++i) {
            auto dir = rand() % DIRS.size();

            // consider the cell adjacent to the
            // blank cell, in the current direction
            auto nextX = blankX + DIRS[dir][0];
            auto nextY = blankY + DIRS[dir][1];
            // if it is inside the board, then move the blank
            if (get(nextX, nextY) != OUT_OF_BOUNDS) {
                moveBlank(dir);
            }
        }
    } while (isFinished());
}

void FifteenPuzzle::move(char symbol)
{
    // for each direction, while symbol not yet found...
    for (auto dir = 0; dir < DIRS.size(); ++dir) {
        // consider the cell next to the blank cell
        auto nextX = blankX + DIRS[dir][0];
        auto nextY = blankY + DIRS[dir][1];
        // if the symbol to move is here...
        if (get(nextX, nextY) == symbol) {
            // move blank this way!
            moveBlank(dir);
            return;
        }
    }
}

void FifteenPuzzle::move(int x, int y)
{
    auto symbol = get(x, y);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(int x, int y) const
{
    auto value = OUT_OF_BOUNDS;
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        value = board[y * cols_ + x];
    }
    return value;
}

void FifteenPuzzle::set(int x, int y, char value)
{
    board[y * cols_ + x] = value;
}

void FifteenPuzzle::moveBlank(int dir)
{
    auto oldX = blankX;
    auto oldY = blankY;
    blankX += DIRS[dir][0];
    blankY += DIRS[dir][1];
    set(oldX, oldY, get(blankX, blankY));
    set(blankX, blankY, BLANK_SYMBOL);
}

bool FifteenPuzzle::isFinished() const
{
    auto correct = true;
    auto expected = FIRST_SYMBOL;
    for (auto y = 0; y < rows_ && correct; ++y) {
        for (auto x = 0; x < cols_ && correct; ++x) {
            auto value = get(x, y);
            // if the cell has the wrong symbol...
            // puzzle is not yet solved!
            if (value != expected && value != BLANK_SYMBOL) {
                correct = false;
            }
            ++expected;
        }
    }
    return correct;
}

string FifteenPuzzle::str() const
{
    ostringstream out;
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            out << get(x, y);
        }
        out << endl;
    }
    out << endl;
    return out.str();
}
