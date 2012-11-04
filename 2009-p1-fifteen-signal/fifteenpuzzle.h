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
#include <complex>
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
    void move(complex<int> pos);
    char get(complex<int> pos) const;
    bool isSolved() const;
    complex<int> getBlank() const;
    complex<int> getMoved() const;
    void write(ostream& out) const;
    FifteenPuzzle(int rows, int columns);

    static const char FIRST_SYMBOL = 'A';
    static const char BLANK_SYMBOL = ' ';
    static const char OUT_OF_BOUNDS = '!';

signals:
    // model signal added
    void blankMoved();

private:
    // silent mode added, for shuffling without emitting signals
    void moveBlank(complex<int> direction, bool silent = false);
    void set(complex<int> pos, char value);

    int columns;
    int rows;
    int size;

    vector<char> board;
    complex<int> blank;
    complex<int> moved;
};

//std::ostream& operator<<(ostream& out, FifteenPuzzle& puzzle);

#endif // FIFTEENPUZZLE_H
