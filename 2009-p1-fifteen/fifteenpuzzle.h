/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef FIFTEENPUZZLE_H
#define FIFTEENPUZZLE_H

#include <iostream>
#include <vector>

class FifteenPuzzle {
public:
    int getColumns() const;
    int getRows() const;
    void init();
    void shuffle();
    void move(char symbol);
    void move(int y, int x);
    char get(int y, int x) const;
    bool isSolved() const;
    void write(std::ostream& out) const;
    FifteenPuzzle(int rows, int columns);

private:
    void moveBlank(int direction);

    const int COLUMNS;
    const int ROWS;
    const int SIZE;

    const static char FIRST_SYMBOL = 'A';
    const static char BLANK_SYMBOL = ' ';
    const static char OUT_OF_BOUNDS = '!';

    std::vector<char> board;
    int blank;

    static const int DIRECTIONS = 4; // N, E, S, W
    static const int DY[DIRECTIONS];
    static const int DX[DIRECTIONS];
};

#endif // FIFTEENPUZZLE_H

//std::ostream& operator<<(std::ostream& out, PuzzleModel& puzzle);
