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
    FifteenPuzzle(int cols, int rows);
    void init(int cols, int rows);
    void shuffle();
    void move(int value);
    void move(Coord cell);
    int get(Coord cell) const;
    bool is_inside(Coord cell) const;
    bool is_finished() const;
    string str() const;

    int cols() const { return cols_; }
    int rows() const { return rows_; }
    Coord blank() const { return blank_; }
    Coord moved() const { return moved_; }

    static const int FIRST = 1;
    static const int BLANK = 0;
private:
    void swap_blank_with(Coord cell);
    void set(Coord cell, int value);

    int cols_;
    int rows_;

    vector<int> board_;
    Coord blank_;  // where's the blank?
    Coord moved_;  // which cell has been moved?

    // DIRS is a vector of couples: (dx, dy)
    const vector<Coord> DIRS = {
        {0, -1}, {-1, 0}, {0, 1}, {1, 0}};
};

#endif // FIFTEENPUZZLE_H
