/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef FIFTEENPUZZLE_H
#define FIFTEENPUZZLE_H

#include <iostream>
#include <vector>

using namespace std;

class FifteenPuzzle
{
public:
    int getColumns() const;
    int getRows() const;
    void init();
    void shuffle();
    void move(char symbol);
    void move(int y, int x);
    char get(int y, int x) const;
    bool isSolved() const;
    void write(ostream& out) const;
    FifteenPuzzle(int rows, int columns);

    static const char FIRST_SYMBOL = 'A';
    static const char BLANK_SYMBOL = ' ';
    static const char OUT_OF_BOUNDS = '!';

private:
    void moveBlank(int direction);
    void set(int y, int x, char value);

    int columns;
    int rows;

    vector<char> board;
    int blankX;
    int blankY;
};

//std::ostream& operator<<(ostream& out, FifteenPuzzle& puzzle);

#endif // FIFTEENPUZZLE_H
