/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEEN_H
#define FIFTEEN_H

#include <string>
#include <vector>

using namespace std;

class Fifteen
{
public:
    Fifteen(int cols, int rows);
    void play_at(int x, int y);
    void flag_at(int x, int y) { }
    string get_val(int x, int y);
    bool finished() { return board_ == solution_; }
    string message() { return "Puzzle solved!"; }
    int cols() { return cols_; }
    int rows() { return rows_; }
private:
    int cols_;
    int rows_;
    int blx_;
    int bly_;

    vector<int> board_;
    vector<int> solution_;
};

#endif // FIFTEEN_H
