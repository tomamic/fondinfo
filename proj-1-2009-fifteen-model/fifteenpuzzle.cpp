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

// N, E, S, W (C++11)
const vector<FifteenPuzzle::Coord> directions = {
    {0, -1}, {+1, 0}, {0, +1}, {-1, 0}};

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
        for (int i = 0; i < rows * rows * columns * columns; ++i) {
            Coord delta = directions[rand() % directions.size()];

            // consider the cell adjacent to the
            // blank cell, in the current direction
            Coord next = blank + delta;
            // if it is inside the board, then move the blank
            if (get(next) != OUT_OF_BOUNDS) {
                moveBlank(delta);
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
    int y = pos.imag(), x = pos.real();
    int value = OUT_OF_BOUNDS;
    if (0 <= y && y < rows && 0 <= x && x < columns) {
        value = board[y * columns + x];
    }
    return value;
}

void FifteenPuzzle::set(Coord pos, char value)
{
    board[pos.imag() * columns + pos.real()] = value;
}

void FifteenPuzzle::moveBlank(Coord delta)
{
    moved = blank;
    blank += delta;
    set(moved, get(blank));
    set(blank, BLANK_SYMBOL);
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

void FifteenPuzzle::write(ostream& out) const
{
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < columns; ++x) {
            out << get({x, y});
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
