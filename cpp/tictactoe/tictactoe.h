#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <vector>
#include <string>

using namespace std;

class BoardGame {
    virtual int rows() = 0;
    virtual int cols() = 0;
    virtual string get_val(int x, int y) = 0;
    virtual void play_at(int x, int y) = 0;
    virtual bool finished() = 0;
    virtual string message() = 0;
};

class TicTacToe : public BoardGame
{
public:
    TicTacToe();
    int rows() { return board_.size(); }
    int cols() { return board_[0].size(); }
    string get_val(int x, int y);
    void play_at(int x, int y);
    bool finished();
    string message();
private:
    bool check_line_(int x, int y, int dx, int dy);
    int turn_ = 0;
    vector< vector<int> > board_ = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
    string msg_ = "Playing";
};

#endif // TICTACTOE_H
