/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteenpuzzle.h"

#include <cstdlib>
#include <sstream>

using namespace std;

// could be static class members
const int NUM_DIRS = 4;
const int DX[] = { 0, +1,  0, -1};
const int DY[] = {-1,  0, +1,  0};

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
    int value = FIRST_SYMBOL;
    for (int y = 0; y < rows_; ++y) {
        for (int x = 0; x < cols_; ++x) {
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
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < rows_ * rows_ * cols_ * cols_; ++i) {
            int dir = rand() % NUM_DIRS;

            // consider the cell adjacent to the
            // blank cell, in the current direction
            int nextX = blankX + DX[dir];
            int nextY = blankY + DY[dir];
            // if it is inside the board, then move the blank
            if (get(nextX, nextY) != OUT_OF_BOUNDS) {
                moveBlank(dir);
            }
        }
    } while (isFinished());
}

void FifteenPuzzle::move(char symbol)
{
    bool found = false;
    // for each direction, while symbol not yet found...
    for (int dir = 0; dir < NUM_DIRS && !found; ++dir) {
        // consider the cell next to the blank cell
        int nextX = blankX + DX[dir];
        int nextY = blankY + DY[dir];
        // if the symbol to move is here...
        if (get(nextX, nextY) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(dir);
        }
    }
}

void FifteenPuzzle::move(int x, int y)
{
    char symbol = get(x, y);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(int x, int y) const
{
    int value = OUT_OF_BOUNDS;
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
    int oldX = blankX;
    int oldY = blankY;
    blankX += DX[dir];
    blankY += DY[dir];
    set(oldX, oldY, get(blankX, blankY));
    set(blankX, blankY, BLANK_SYMBOL);
}

bool FifteenPuzzle::isFinished() const
{
    bool correct = true;
    char expected = FIRST_SYMBOL;
    for (int y = 0; y < rows_ && correct; ++y) {
        for (int x = 0; x < cols_ && correct; ++x) {
            char value = get(x, y);
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
    for (int y = 0; y < rows_; ++y) {
        for (int x = 0; x < cols_; ++x) {
            out << get(x, y);
        }
        out << endl;
    }
    out << endl;
    return out.str();
}
