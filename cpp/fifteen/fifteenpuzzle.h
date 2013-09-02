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

typedef complex<int> Coord;

class FifteenPuzzle
{
public:
    int cols() const { return cols_; }
    int rows() const { return rows_; }
    Coord blank() const { return blank_; }
    Coord moved() const { return moved_; }

    void sort();
    void shuffle();
    void move(char symbol);
    void move(Coord pos);
    char get(Coord pos) const;
    bool finished() const;
    string str() const;
    FifteenPuzzle(int cols, int rows);

    static const char FIRST = 'A';
    static const char BLANK = ' ';
    static const char OUT_OF_BOUNDS = '!';

private:
    void moveBlank(Coord dir);
    void set(Coord pos, char value);

    int cols_;
    int rows_;

    vector<char> board_;
    Coord blank_;
    Coord moved_;

    // DIRS is a vector of couples: (dx, dy)
    const vector<Coord> DIRS = {
        {0, -1}, {-1, 0}, {0, 1}, {1, 0}};
};

#endif // FIFTEENPUZZLE_H
