/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
            set({x, y}, value);
            ++value;
        }
    }
    // put blank in the last cell
    blank = {cols - 1, rows - 1};
    set(blank, BLANK_SYMBOL);
    moved = blank;
}

void FifteenPuzzle::shuffle()
{
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < rows * rows * cols * cols; ++i) {
            Coord delta = directions[rand() % directions.size()];

            // consider the cell adjacent to the
            // blank cell, in the current direction
            Coord next = blank + delta;
            // if it is inside the board, then move the blank
            if (get(next) != OUT_OF_BOUNDS) {
                moveBlank(delta);
            }
        }
    } while (isFinished());
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
    if (0 <= y && y < rows && 0 <= x && x < cols) {
        value = board[y * cols + x];
    }
    return value;
}

void FifteenPuzzle::set(Coord pos, char value)
{
    board[pos.imag() * cols + pos.real()] = value;
}

void FifteenPuzzle::moveBlank(Coord delta)
{
    moved = blank;
    blank += delta;
    set(moved, get(blank));
    set(blank, BLANK_SYMBOL);
}

bool FifteenPuzzle::isFinished() const
{
    bool correct = true;
    char expected = FIRST_SYMBOL;
    for (int y = 0; y < rows && correct; ++y) {
        for (int x = 0; x < cols && correct; ++x) {
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
        for (int x = 0; x < cols; ++x) {
            out << get({x, y});
        }
        out << endl;
    }
    out << endl;
}
