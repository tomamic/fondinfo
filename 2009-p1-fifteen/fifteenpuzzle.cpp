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
#include <algorithm>

using namespace std;

const int FifteenPuzzle::DY[] = { -1,  0, +1,  0}; // N, E, S, W
const int FifteenPuzzle::DX[] = {  0, +1,  0, -1}; // N, E, S, W

FifteenPuzzle::FifteenPuzzle(int rows, int columns)
{
    this->rows = rows;
    this->columns = columns;
    size = columns * rows;
    board.assign(size, ' ');

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
    for (int i = 0; i < size; ++i) {
        board[i] = i + FIRST_SYMBOL;
    }
    // put blank in the last cell
    blank = size - 1;
    board[blank] = BLANK_SYMBOL;
}

void FifteenPuzzle::shuffle()
{
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < size * size; ++i) {
            int direction = rand() % DIRECTIONS;

            // consider the cell adjacent to the
            // blank cell, in the current direction
            int nextY = (blank / columns) + DY[direction];
            int nextX = (blank % columns) + DX[direction];
            // if it is inside the board, then move the blank
            if (0 <= nextY && nextY < rows && 0 <= nextX && nextX < columns) {
                moveBlank(direction);
            }
        }
    } while (isSolved());
}

void FifteenPuzzle::move(char symbol)
{
    bool found = false;
    // for each direction, while symbol not yet found...
    for (int direction = 0; direction < DIRECTIONS && !found; ++direction) {
        // consider the cell adjacent to the
        // blank cell, in the current direction
        int nextY = (blank / columns) + DY[direction];
        int nextX = (blank % columns) + DX[direction];
        // if the symbol to move is here...
        if (get(nextY, nextX) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(direction);
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

void FifteenPuzzle::moveBlank(int direction)
{
    int old = blank;
    blank += DY[direction] * columns + DX[direction];
    board[old] = board[blank];
    board[blank] = BLANK_SYMBOL;
}

bool FifteenPuzzle::isSolved() const
{
    bool solved = true;
    // for each cell (ltr, ttb), but the last one...
    for (int i = 0; i < size - 1 && solved; ++i) {
        // if it has the wrong symbol...
        // puzzle is not yet solved!
        solved = (board[i] == i + FIRST_SYMBOL);
    }
    return solved;
}

void FifteenPuzzle::write(ostream& out) const
{
    for (int i = 0; i < size; ++i) {
        out << board[i];
        if (i % columns == columns - 1) {
            out << endl;
        }
    }
    out << endl;
}

//ostream& operator<<(ostream& out, FifteenPuzzle& puzzle)
//{
//    puzzle.write(out);
//    return out;
//}
