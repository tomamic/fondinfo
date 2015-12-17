#ifndef SLITHERLINK_H
#define SLITHERLINK_H

#include "game.h"
#include <vector>
#include <complex>

typedef std::complex<int> Coord;

class Slitherlink : public Game
{
public:
    Slitherlink();
    Slitherlink(std::string filename);
//    void write(std::string filename) const;
    virtual void play_at(int x, int y);
    virtual int cols() const {return cols_; }
    virtual int rows() const { return rows_; }
    virtual std::string get_val(int x, int y) const;
    virtual bool finished() const;
    virtual std::string message() const { return "Puzzle solved"; }
    int count_first_loop();
    int count_loop(Coord pos, Coord dir, Coord stop, int lines) const;
    bool check_sign(Coord pos, char sign) const;
    std::string str() const;
private:
    int cols_ = 0;
    int rows_ = 0;
    std::vector< std::vector<char> > board_;
};

#endif // SLITHERLINK_H
