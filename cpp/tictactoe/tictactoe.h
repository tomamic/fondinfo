#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <vector>
#include <string>

using namespace std;

class TicTacToe
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
