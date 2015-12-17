#include "slitherlink.h"
#include <fstream>

using namespace std;

std::vector<Coord> moves = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

Slitherlink::Slitherlink()
{
    cols_ = 11;
    rows_ = 11;
    board_ = {
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
}

Slitherlink::Slitherlink(string filename)
{
    ifstream in{filename};
    string line;
    while (getline(in, line) && line != "") {
        board_.push_back({begin(line), end(line)});
//        vector<char> chars;
//        for (auto c: line) {
//            chars.push_back(c);
//        }
//        board_.push_back(chars);
    }
    rows_ = board_.size();
    if (rows_ > 0) cols_ = board_[0].size();
}

void Slitherlink::play_at(int x, int y)
{
    if ((x + y) % 2 == 1) {
        board_[y][x] = '-';
    }
}

std::string Slitherlink::get_val(int x, int y) const
{
    // conversion from char to string
    // char val = '5';  /* just for example ... */
    // string txt = string(1, val);
    
    /* ADD YOUR CODE HERE */
    return string(1, board_[y][x]);
}

bool Slitherlink::finished() const
{
    // conversion from char to int
    // char val = '5';  /* just for example ... */
    // int num = val - '0';
    
    /* ADD YOUR CODE HERE */
    return false;
}


int Slitherlink::count_first_loop()
{
    auto len = 0;
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            if (board_[y][x] == '-') {
                return count_loop({x + 1, y}, {1, 0}, {x + 1, y}, 0);
            }
        }
    }
    return len;
}

bool Slitherlink::check_sign(Coord pos, char sign) const
{
    auto result = false;
    auto x = pos.real(), y = pos.imag();
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        result = (board_[y][x] == sign);
    }
    return result;
}

string Slitherlink::str() const
{
    ostringstream out;
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            out << board_[y][x];
        }
        out << endl;
    }
    return out.str();
}

int Slitherlink::count_loop(Coord pos, Coord dir, Coord stop, int lines) const
{
    if (pos == stop && lines > 0) return lines;

    // TODO: pay attention to crossroads and branches!
    for (auto move : moves) {
        if (move != -dir && check_sign(pos + move, '-')) {
            return count_loop(pos + 2 * move, move, stop, lines + 1);
            // tail recursion
        }
    }
    return 0;  // this way, open paths may be considered
}

//int Slitherlink::count_loop_iter(Coord pos, Coord dir,
//                                 Coord stop, int lines) const {
//    while (pos != stop || lines == 0) {
//        for (auto move : moves) {
//            if (move != -dir && check_sign(pos + move, '-')) {
//                pos += 2 * move; dir = move; lines += 1;
//                break;
//            }
//        }
//    }
//    return lines;
//}
