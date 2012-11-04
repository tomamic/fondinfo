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

// N, E, S, W
const vector<FifteenPuzzle::Coord> directions = {
    {0, -1}, {+1, 0}, {0, +1}, {-1, 0}};

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
    moved = blank;
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
            Coord next = blank + directions[d];
            // if it is inside the board, then move the blank
            if (get(next) != OUT_OF_BOUNDS) {
                moveBlank(directions[d], true); // silent, no signals emitted
            }
        }
    } while (isSolved());
}

void FifteenPuzzle::move(char symbol)
{
    // for each direction, while symbol not yet found...
    for (Coord delta : directions) {
        // consider the cell adjacent to the
        // blank cell, in the current direction
        Coord next = blank + delta;
        // if the symbol to move is here...
        if (get(next) == symbol) {
            // move blank this way!
            moveBlank(delta);
            break;
        }
    }
}

void FifteenPuzzle::move(Coord pos)
{
    char symbol = get(pos);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(Coord pos) const
{
    int value = OUT_OF_BOUNDS;
    if (0 <= pos.imag() && pos.imag() < rows
            && 0 <= pos.real() && pos.real() < columns) {
        value = board[pos.imag() * columns + pos.real()];
    }
    return value;
}

void FifteenPuzzle::set(Coord pos, char value)
{
    board[pos.imag() * columns + pos.real()] = value;
}

void FifteenPuzzle::moveBlank(Coord direction, bool silent)
{
    moved = blank;
    blank += direction;
    set(moved, get(blank));
    set(blank, BLANK_SYMBOL);
    // while shuffling, no signals are emitted
    if (! silent) {
        emit blankMoved();
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

FifteenPuzzle::Coord FifteenPuzzle::getBlank() const
{
    return blank;
}

FifteenPuzzle::Coord FifteenPuzzle::getMoved() const
{
    return moved;
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
