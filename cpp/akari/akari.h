#ifndef AKARI_H
#define AKARI_H

#include <vector>
#include <complex>

using namespace std;

class Akari
{
public:
    Akari();
    void play_at(int x, int y);
    string get_val(int x, int y);
    bool finished();
    string to_string();

    int cols() {return cols_; }
    int rows() { return rows_; }
    string message() { return "Puzzle solved"; }

    static const char EMPTY = ' ';
    static const char BULB  = '@';
    static const char FLAG  = 'x';
    static const char LIGHT = '+';
//    static const char WALL0 = '0';
//    static const char WALL1 = '1';
//    static const char WALL2 = '2';
//    static const char WALL3 = '3';
//    static const char WALL4 = '4';
//    static const char WALL  = '5';

private:
    int cols_ = 7;
    int rows_ = 7;
    vector< vector<char> > board_ = {
        {' ', ' ', ' ', '5', '5', '1', ' '},
        {' ', '5', ' ', ' ', ' ', ' ', ' '},
        {'1', ' ', ' ', '5', ' ', '0', ' '},
        {' ', '5', ' ', ' ', ' ', '5', ' '},
        {' ', '1', ' ', '3', ' ', ' ', '2'},
        {' ', ' ', ' ', ' ', ' ', '2', ' '},
        {' ', '5', '5', '5', ' ', ' ', ' '} };
    // '5' is for unnumbered walls:
    // no constraint on surrounding bulbs
};

#endif // AKARI_H
