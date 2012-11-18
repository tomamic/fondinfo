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
    int getCols() const;
    int getRows() const;
    void sort();
    void shuffle();
    void move(char symbol);
    void move(int y, int x);
    char get(int y, int x) const;
    bool isFinished() const;
    void write(ostream& out) const;
    FifteenPuzzle(int rows, int cols);

    static const char FIRST_SYMBOL = 'A';
    static const char BLANK_SYMBOL = ' ';
    static const char OUT_OF_BOUNDS = '!';

private:
    void moveBlank(int dir);
    void set(int y, int x, char value);

    int cols;
    int rows;

    vector<char> board;
    int blankX;
    int blankY;
};

//std::ostream& operator<<(ostream& out, FifteenPuzzle& puzzle);

#endif // FIFTEENPUZZLE_H
