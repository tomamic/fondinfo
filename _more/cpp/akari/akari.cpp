#include "akari.h"
#include <fstream>

vector<vector<int>> dirs4 = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

Akari::Akari()
{
}

Akari::Akari(string filename)
{
    ifstream file{filename};
    if (file.good()) {
        board_ = {};
        string line;
        while (getline(file, line)) {
            vector<char> row;
            for (auto c : line) row.push_back(c);
            cols_ = row.size();
            board_.push_back(row);
        }
        rows_ = board_.size();
    }
}

void Akari::play_at(int x, int y)
{
    /* ADD YOUR CODE HERE */
    board_[y][x] = BULB;

    for (auto d : dirs4) {
        auto dx = d[0], dy = d[1];
        auto x1 = x + dx, y1 = y + dy;
        while (is_white(x1, y1)) {
            board_[y1][x1] = LIGHT;
            x1 += dx; y1 += dy;
        }
    }
}

std::string Akari::get_val(int x, int y)
{
    // conversion from char to string
    // char val = '5';  /* just for example ... */
    // string txt = string(1, val);
    
    /* ADD YOUR CODE HERE */
    return string(1, board_[y][x]);
}

bool Akari::finished()
{
    // conversion from char to int
    // char val = '4';  /* just for example ... */
    // int num = val - '0';
    
    /* ADD YOUR CODE HERE */
    return false;
}

string Akari::to_string()
{
    /* ADD YOUR CODE HERE */
    return "";
}

bool Akari::is_white(int x, int y)
{
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        return ! ('0' <= board_[y][x] && board_[y][x] <= '5');
    }
    return false;
}
