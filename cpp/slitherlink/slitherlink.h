#ifndef SLITHERLINK_H
#define SLITHERLINK_H

#include "game.h"
#include <vector>

class Slitherlink : public Game
{
public:
    Slitherlink();
    virtual void play_at(int x, int y);
    virtual int cols() const {return cols_; }
    virtual int rows() const { return rows_; }
    virtual std::string get_val(int x, int y) const;
    virtual bool finished() const;
    virtual std::string message() const { return "Puzzle solved"; }
private:
    int cols_ = 11;
    int rows_ = 11;
    std::vector< std::vector<char> > board_ = {
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'},
        {' ', ' ', ' ', '3', ' ', '2', ' ', '2', ' ', ' ', ' '},
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'},
        {' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', '2', ' '},
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'},
        {' ', ' ', ' ', '2', ' ', ' ', ' ', ' ', ' ', '1', ' '},
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'},
        {' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', '2', ' '},
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'},
        {' ', ' ', ' ', '2', ' ', ' ', ' ', '2', ' ', ' ', ' '},
        {'+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+'} };
};

#endif // SLITHERLINK_H
