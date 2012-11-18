/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef BOARD_H
#define BOARD_H

#include <iostream>
#include <vector>

using namespace std;

class Board
{
public:
    Board(int height, int width);
    bool solve();
    void write(ostream &out);

private:
    bool placeQueens(int row);
    bool underAttack(int row, int col);

    int height;
    int width;
    vector< vector<bool> > board;
};

#endif // BOARD_H
