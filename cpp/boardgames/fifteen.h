/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEEN_H
#define FIFTEEN_H

#include "boardgame.h"
#include <string>
#include <vector>
using namespace std;

class Fifteen : public BoardGame
{
public:
    Fifteen(int w, int h);
    void play_at(int x, int y);
    void flag_at(int x, int y) { }
    string get_val(int x, int y);
    bool finished() { return board_ == solved_; }
    string message() { return "Puzzle solved!"; }
    int cols() { return w_; }
    int rows() { return h_; }
private:
    int pos(int x, int y) { return y * w_ + x; }
    int w_, h_;
    int x0_, y0_;  // blank
    vector<int> board_, solved_;
};

#endif // FIFTEEN_H
