/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEENPUZZLE_H
#define FIFTEENPUZZLE_H

#include <iostream>
#include <vector>

using namespace std;

class FifteenPuzzle
{
public:
    int cols() const;
    int rows() const;
    void sort();
    void shuffle();
    void move(char symbol);
    void move(int x, int y);
    char get(int x, int y) const;
    bool isFinished() const;
    string str() const;
    FifteenPuzzle(int cols, int rows);

    static const char FIRST_SYMBOL = 'A';
    static const char BLANK_SYMBOL = ' ';
    static const char OUT_OF_BOUNDS = '!';

private:
    void moveBlank(int dir);
    void set(int x, int y, char value);

    int cols_;
    int rows_;

    vector<char> board;
    int blankX;
    int blankY;
};

//std::ostream& operator<<(ostream& out, FifteenPuzzle& puzzle);

#endif // FIFTEENPUZZLE_H
