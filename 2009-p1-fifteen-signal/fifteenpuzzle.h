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
#include <QtCore/QObject>

using namespace std;

class FifteenPuzzle : public QObject {
    Q_OBJECT

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

    const static char FIRST_SYMBOL = 'A';
    const static char BLANK_SYMBOL = ' ';
    const static char OUT_OF_BOUNDS = '!';

signals:
    // model signal added
    void blankMoved(int newY, int newX, int oldY, int oldX);

private:
    // silent mode added, for shuffling without emitting signals
    void moveBlank(int direction, bool silent = false);

    int columns;
    int rows;
    int size;

    vector<char> board;
    int blank;

    static const int DIRECTIONS = 4; // N, E, S, W
    static const int DY[DIRECTIONS];
    static const int DX[DIRECTIONS];
};

//std::ostream& operator<<(ostream& out, FifteenPuzzle& puzzle);

#endif // FIFTEENPUZZLE_H
