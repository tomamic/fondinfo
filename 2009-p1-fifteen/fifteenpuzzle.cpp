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
const int DY = 0, DX = 1; // N, E, S, W
const vector< vector<int> > directions = {
    {-1, 0}, {0, +1}, {+1, 0}, {0, -1}};

FifteenPuzzle::FifteenPuzzle(int rows, int columns)
{
    if (rows < 2) { rows = 2; }
    if (columns < 2) { columns = 2; }
    this->rows = rows;
    this->columns = columns;
    board.assign(rows * columns, BLANK_SYMBOL);

    init();
    shuffle();
}

int FifteenPuzzle::getColumns() const
{
    return columns;
}

int FifteenPuzzle::getRows() const
{
    return rows;
}

void FifteenPuzzle::init()
{
    // put ordered symbols in each cell (ltr, ttb)
    int value = FIRST_SYMBOL;
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < columns; ++x) {
            set(y, x, value);
            ++value;
        }
    }
    // put blank in the last cell
    blankY = rows - 1;
    blankX = columns - 1;
    set(blankY, blankX, BLANK_SYMBOL);
}

void FifteenPuzzle::shuffle()
{
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < rows * rows * columns * columns; ++i) {
            int d = rand() % directions.size();

            // consider the cell adjacent to the
            // blank cell, in the current direction
            int nextY = blankY + directions[d][DY];
            int nextX = blankX + directions[d][DX];
            // if it is inside the board, then move the blank
            if (0 <= nextY && nextY < rows
                    && 0 <= nextX && nextX < columns) {
                moveBlank(d);
            }
        }
    } while (isSolved());
}

void FifteenPuzzle::move(char symbol)
{
    bool found = false;
    // for each direction, while symbol not yet found...
    for (int d = 0; d < directions.size() && !found; ++d) {
        // consider the cell adjacent to the
        // blank cell, in the current direction
        int nextY = blankY + directions[d][DY];
        int nextX = blankX + directions[d][DX];
        // if the symbol to move is here...
        if (get(nextY, nextX) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(d);
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
    if (0 <= y && y < rows && 0 <= x && x < columns) {
        value = board[y * columns + x];
    }
    return value;
}

void FifteenPuzzle::set(int y, int x, char value)
{
    board[y * columns + x] = value;
}

void FifteenPuzzle::moveBlank(int direction)
{
    int oldY = blankY;
    int oldX = blankX;
    blankY += directions[direction][DY];
    blankX += directions[direction][DX];
    set(oldY, oldX, get(blankY, blankX));
    set(blankY, blankX, BLANK_SYMBOL);
}

bool FifteenPuzzle::isSolved() const
{
    bool correct = true;
    char expected = FIRST_SYMBOL;
    for (int y = 0; y < rows && correct; ++y) {
        for (int x = 0; x < columns && correct; ++x) {
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
        for (int x = 0; x < columns; ++x) {
            out << get(y, x);
        }
        out << endl;
    }
    out << endl;
}

//ostream& operator<<(ostream& out, FifteenPuzzle& puzzle)
//{
//    puzzle.write(out);
//    return out;
//}
