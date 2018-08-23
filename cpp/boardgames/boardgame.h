#ifndef BOARDGAME_H
#define BOARDGAME_H

#include <string>

class BoardGame
{
public:
    virtual void play_at(int x, int y) = 0;
    virtual void flag_at(int x, int y) = 0;
    virtual int cols() = 0;
    virtual int rows() = 0;
    virtual std::string get_val(int x, int y) = 0;
    virtual bool finished() = 0;
    virtual std::string message() = 0;

    virtual ~BoardGame() {}
};

#endif // BOARDGAME_H
