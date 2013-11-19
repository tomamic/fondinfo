#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <string>
#include <vector>

using namespace std;

class TicTacToe
{
public:
    static const char NONE = '.';
    static const char PLR1 = 'X';
    static const char PLR2 = 'O';
    static const char DRAW = 'N';
    static const char OUT = '!';

    TicTacToe(int side);
    void clear();
    void play_at(int x, int y);
    char get(int x, int y);
    bool check_line(int x, int y, int dx, int dy);
    char winner();
    int side();
    string str();
private:
    int side_;
    int turn_;
    vector<char> matrix_;
};

#endif // TICTACTOE_H
