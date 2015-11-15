/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEEN_H
#define FIFTEEN_H

#include "game.h"
#include <iostream>
#include <vector>
#include <complex>

using namespace std;

typedef complex<int> Coord;

class Fifteen : public Game
{
public:
    Fifteen(int cols, int rows);
    void init(int cols, int rows);
    void new_game();
    void move_val(int value);
    int get(int x, int y) const;
    Coord blank() const { return blank_; }
    Coord moved() const { return moved_; }
    string str() const;

    void play_at(int x, int y) override;
    std::string get_val(int x, int y) const override;
    bool finished() const override;
    std::string message() const override { return "Puzzle solved!"; }
    int cols() const override { return cols_; }
    int rows() const override { return rows_; }
private:
    void swap_blank_with(int x, int y);

    int cols_;
    int rows_;

    vector<int> board_;
    Coord blank_;  // where's the blank?
    Coord moved_;  // which cell has been moved?

    // DIRS is a vector of couples: (dx, dy)
    const vector<Coord> DIRS = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
};

#endif // FIFTEEN_H
