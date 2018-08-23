#ifndef LIGHTSOUT_H
#define LIGHTSOUT_H

#include "boardgame.h"
#include <vector>

class LightsOut : public BoardGame
{
public:
    LightsOut(int level, int cols, int rows);
    void play_at(int x, int y);
    void flag_at(int x, int y) { }
    std::string get_val(int x, int y);
    bool finished();
    int cols() { return rows_; }
    int rows() { return cols_; }
    std::string message() { return "Solved!"; }
private:
    std::vector<std::vector<bool>> board_;
    int cols_;
    int rows_;
};

#endif // LIGHTSOUT_H
