/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEENPUZZLE_H
#define FIFTEENPUZZLE_H

#include <iostream>
#include <vector>
#include <complex>

using namespace std;

class FifteenPuzzle
{
public:
    typedef complex<int> Coord;
    FifteenPuzzle(int rows, int cols);
    virtual int getCols() const;
    virtual int getRows() const;
    virtual void sort();
    virtual void shuffle();
    virtual void move(char symbol);
    virtual void move(Coord pos);
    virtual char get(Coord pos) const;
    virtual bool isFinished() const;
    virtual void write(ostream& out) const;

    static const char FIRST_SYMBOL = 'A';
    static const char BLANK_SYMBOL = ' ';
    static const char OUT_OF_BOUNDS = '!';

protected:
    virtual void moveBlank(Coord delta);
    virtual void set(Coord pos, char value);

    int cols;
    int rows;

    vector<char> board;
    Coord blank;
    Coord moved;
};

#endif // FIFTEENPUZZLE_H
