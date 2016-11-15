#include "tictactoe.h"

TicTacToe::TicTacToe()
{

}

string TicTacToe::get_val(int x, int y)
{
    string val = " ";
    if (0 <= x && x < cols() && 0 <= y && y < rows()) {
        if (board_[y][x] == 1) {
            val = "X";
        } else if (board_[y][x] == 2) {
            val = "O";
        }
    }
    return val;
}

void TicTacToe::play_at(int x, int y)
{
    if (0 <= x && x < cols() && 0 <= y && y < rows() && board_[y][x] == 0) {
        board_[y][x] = 1 + turn_ % 2;
        turn_ += 1;
    }
}

bool TicTacToe::check_line_(int x, int y, int dx, int dy) {
    auto first = get_val(x, y);
    if (first == " ") return false;
    while (0 <= x && x < cols() && 0 <= y && y < rows()) {
        if (get_val(x, y) != first) return false;
        x += dx;
        y += dy;
    }
    msg_ = first + " won";
    return true;
}

bool TicTacToe::finished()
{
    if (turn_ == rows() * cols()) {
        msg_ = "Draw";
        return true;
    }
    for (auto x = 0; x < cols(); ++x) {
        if (check_line_(x, 0, 0, +1)) return true;
    }
    for (auto y = 0; y < rows(); ++y) {
        if (check_line_(0, y, +1, 0)) return true;
    }
    if (check_line_(0, 0, +1, +1)) return true;
    if (check_line_(0, rows() - 1, +1, -1)) return true;
    return false;
}

string TicTacToe::message()
{
    return msg_;
}
