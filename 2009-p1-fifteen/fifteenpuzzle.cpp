/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteenpuzzle.h"

#include <cstdlib>
#include <algorithm>

const int FifteenPuzzle::DY[] = { -1,  0, +1,  0}; // N, E, S, W
const int FifteenPuzzle::DX[] = {  0, +1,  0, -1}; // N, E, S, W

FifteenPuzzle::FifteenPuzzle(int rows, int columns) :
    ROWS(rows),
    COLUMNS(columns),
    SIZE(COLUMNS * ROWS),
    board(SIZE)
{
    init();
    shuffle();
}

int FifteenPuzzle::getColumns() const {
    return COLUMNS;
}

int FifteenPuzzle::getRows() const {
    return ROWS;
}

void FifteenPuzzle::init() {
    // put ordered symbols in each cell (ltr, ttb)
    for (int i = 0; i < SIZE; ++i) {
        board[i] = i + FIRST_SYMBOL;
    }
    // put blank in the last cell
    blank = SIZE - 1;
    board[blank] = BLANK_SYMBOL;
}

void FifteenPuzzle::shuffle() {
    do {
        // generate SIZE^2 random directions
        // for a random walk of the blank cell
        for (int i = 0; i < SIZE * SIZE; ++i) {
            int direction = rand() % DIRECTIONS;

            // consider the cell adjacent to the
            // blank cell, in the current direction
            int nextY = (blank / COLUMNS) + DY[direction];
            int nextX = (blank % COLUMNS) + DX[direction];
            // if it is inside the board, then move the blank
            if (0 <= nextY && nextY < ROWS && 0 <= nextX && nextX < COLUMNS) {
                moveBlank(direction);
            }
        }
    } while (isSolved());
}

void FifteenPuzzle::move(char symbol) {
    bool found = false;
    // for each direction, while symbol not yet found...
    for (int direction = 0; direction < DIRECTIONS && !found; ++direction) {
        // consider the cell adjacent to the
        // blank cell, in the current direction
        int nextY = (blank / COLUMNS) + DY[direction];
        int nextX = (blank % COLUMNS) + DX[direction];
        // if the symbol to move is here...
        if (get(nextY, nextX) == symbol) {
            found = true;
            // move blank this way!
            moveBlank(direction);
        }
    }
}

void FifteenPuzzle::move(int y, int x) {
    char symbol = get(y, x);
    if (symbol != OUT_OF_BOUNDS) {
        move(symbol);
    }
}

char FifteenPuzzle::get(int y, int x) const {
    int value = OUT_OF_BOUNDS;
    if (0 <= y && y < ROWS && 0 <= x && x < COLUMNS) {
        value = board[y * COLUMNS + x];
    }
    return value;
}

void FifteenPuzzle::moveBlank(int direction) {
    int old = blank;
    blank += DY[direction] * COLUMNS + DX[direction];
    board[old] = board[blank];
    board[blank] = BLANK_SYMBOL;
}

bool FifteenPuzzle::isSolved() const {
    bool solved = true;
    // for each cell (ltr, ttb), but the last one...
    for (int i = 0; i < SIZE - 1 && solved; ++i) {
        // if it has the wrong symbol...
        // puzzle is not yet solved!
        solved = (board[i] == i + FIRST_SYMBOL);
    }
    return solved;
}

void FifteenPuzzle::write(std::ostream& out) const {
    for (int i = 0; i < SIZE; ++i) {
        out << board[i];
        if (i % COLUMNS == COLUMNS - 1) {
            out << std::endl;
        }
    }
    out << std::endl;
}

//std::ostream& operator<<(std::ostream& out, PuzzleModel& puzzle) {
//    puzzle.write(out);
//    return out;
//}
