/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
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
