/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <sstream>

using namespace std;

void printBoard(bool board[], const int SIDE, ostream &out)
{
    for (int y = 0; y < SIDE; ++y) {
        for (int x = 0; x < SIDE; ++x) {
            out << '|' << (board[y * SIDE + x] ? 'Q' : ' ');
        }
        out << '|' << endl;
    }
    out << endl << endl;
}

bool underAttack(bool board[], const int SIDE, int row, int col)
{
    static const int DIRECTIONS = 8;
    static const int DY[] = {-1,-1, 0, 1, 1, 1, 0,-1}; // N, NE, E, SE, S, SW, W, NW
    static const int DX[] = { 0, 1, 1, 1, 0,-1,-1,-1}; // N, NE, E, SE, S, SW, W, NW

    bool attack = false;
    for (int dir = 0; dir < DIRECTIONS && !attack; ++dir) {
        int y = row + DY[dir];
        int x = col + DX[dir];
        while (0 <= y && y < SIDE && 0 <= x && x < SIDE && !attack) {
            attack = board[y * SIDE + x];
            y += DY[dir];
            x += DX[dir];
        }
    }
    return attack;
}

bool placeQueens(bool board[], const int SIDE, int row)
{
    bool result = false;
    for (int col = 0; col < SIDE && !result; ++col) {
        if (!underAttack(board, SIDE, row, col)) {
            board[row * SIDE + col] = true;
            if (row == SIDE-1) {
                result = true;
            } else {
                result = placeQueens(board, SIDE, row+1);
            }
            if (!result) board[row * SIDE + col] = false; // backtracking
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    const int SIDE = 6;
    bool board[SIDE*SIDE];
    for (int i = 0; i < SIDE*SIDE; ++i) {
        board[i] = false;
    }

    placeQueens(board, SIDE, 0);
    printBoard(board, SIDE, cout);

    return 0;
}
