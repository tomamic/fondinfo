/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteenpuzzle.h"

#include <cstdlib>

using namespace std;

// could be static class members
const int NUM_DIRS = 4;
const int DY[] = {-1,  0, +1,  0};
const int DX[] = { 0, +1,  0, -1};

FifteenPuzzle::FifteenPuzzle(int rows, int columns)
{
    if (rows < 2) { rows = 2; }
    if (columns < 2) { columns = 2; }
    this->rows = rows;
    this->cols = columns;
    board.assign(rows * columns, BLANK_SYMBOL);

    sort();
    shuffle();
}

int FifteenPuzzle::getCols() const
{
    return cols;
}

int FifteenPuzzle::getRows() const
{
    return rows;
}

void FifteenPuzzle::sort()
{
    // put ordered symbols in each cell (ltr, ttb)
    int value = FIRST_SYMBOL;
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < cols; ++x) {
            set(y, x, value);
            ++value;
        }
    }
    // put blank in the last cell
    blankY = rows - 1;
    blankX = cols - 1;
    set(blankY, blankX, BLANK_SYMBOL);
}

void FifteenPuzzle::shuffle()
{
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < rows * rows * cols * cols; ++i) {
            int dir = rand() % NUM_DIRS;

            // consider the cell adjacent to the
            // blank cell, in the current direction
            int nextY = blankY + DY[dir];
            int nextX = blankX + DX[dir];
            // if it is inside the board, then move the blank
            if (get(nextY, nextX) != OUT_OF_BOUNDS) {
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
        int nextY = blankY + DY[dir];
        int nextX = blankX + DX[dir];
        // if the symbol to move is here...
        if (get(nextY, nextX) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(dir);
        }
    }
}

void FifteenPuzzle::move(int y, int x)
{
    char symbol = get(y, x);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(int y, int x) const
{
    int value = OUT_OF_BOUNDS;
    if (0 <= y && y < rows && 0 <= x && x < cols) {
        value = board[y * cols + x];
    }
    return value;
}

void FifteenPuzzle::set(int y, int x, char value)
{
    board[y * cols + x] = value;
}

void FifteenPuzzle::moveBlank(int dir)
{
    int oldY = blankY;
    int oldX = blankX;
    blankY += DY[dir];
    blankX += DX[dir];
    set(oldY, oldX, get(blankY, blankX));
    set(blankY, blankX, BLANK_SYMBOL);
}

bool FifteenPuzzle::isFinished() const
{
    bool correct = true;
    char expected = FIRST_SYMBOL;
    for (int y = 0; y < rows && correct; ++y) {
        for (int x = 0; x < cols && correct; ++x) {
            char value = get(y, x);
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

void FifteenPuzzle::write(ostream& out) const
{
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < cols; ++x) {
            out << get(y, x);
        }
        out << endl;
    }
    out << endl;
}

//ostream& operator<<(ostream& out, const FifteenPuzzle& puzzle)
//{
//    puzzle.write(out);
//    return out;
//}
