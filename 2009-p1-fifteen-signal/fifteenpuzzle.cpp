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

// W, S, E, N (C++11)
const vector< complex<int> > directions = {
    {-1,  0}, { 0, +1}, {+1,  0}, { 0, -1}};

FifteenPuzzle::FifteenPuzzle(int rows, int columns)
{
    if (rows < 2) rows = 2;
    if (columns < 2) columns = 2;
    this->rows = rows;
    this->columns = columns;
    size = columns * rows;
    board.assign(size, BLANK_SYMBOL);

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
            set({x, y}, value);
            ++value;
        }
    }
    // put blank in the last cell
    blank = {columns - 1, rows - 1};
    set(blank, BLANK_SYMBOL);
}

void FifteenPuzzle::shuffle()
{
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < size * size; ++i) {
            int d = rand() % directions.size();

            // consider the cell adjacent to the
            // blank cell, in the current direction
            complex<int> next = blank + directions[d];
            // if it is inside the board, then move the blank
            if (get(next) != OUT_OF_BOUNDS) {
                moveBlank(directions[d], true); // silent, no signals emitted
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
        complex<int> next = blank + directions[d];
        // if the symbol to move is here...
        if (get(next) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(directions[d]);
        }
    }
}

void FifteenPuzzle::move(complex<int> pos)
{
    char symbol = get(pos);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(complex<int> pos) const
{
    int value = OUT_OF_BOUNDS;
    if (0 <= pos.imag() && pos.imag() < rows
            && 0 <= pos.real() && pos.real() < columns) {
        value = board[pos.imag() * columns + pos.real()];
    }
    return value;
}

void FifteenPuzzle::set(complex<int> pos, char value)
{
    board[pos.imag() * columns + pos.real()] = value;
}

void FifteenPuzzle::moveBlank(complex<int> direction, bool silent)
{
    complex<int> old = blank;
    blank += direction;
    set(old, get(blank));
    set(blank, BLANK_SYMBOL);
    // while shuffling, no signals are emitted
    if (! silent) {
        emit blankMoved(blank.imag(), blank.real(), old.imag(), old.real());
    }
}

bool FifteenPuzzle::isSolved() const
{
    bool correct = true;
    char expected = FIRST_SYMBOL;
    for (int y = 0; y < rows && correct; ++y) {
        for (int x = 0; x < columns && correct; ++x) {
            char value = get({x, y});
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

void FifteenPuzzle::write(std::ostream& out) const
{
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < columns; ++x) {
            out << get({x, y});
        }
        out << endl;
    }
    out << endl;
}

//std::ostream& operator<<(std::ostream& out, FifteenPuzzle& puzzle)
//{
//    puzzle.write(out);
//    return out;
//}
