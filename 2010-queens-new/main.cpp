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

void printBoard(bool** board, int side, ostream &out)
{
    for (int y = 0; y < side; ++y) {
        for (int x = 0; x < side; ++x) {
            out << '|' << (board[y][x] ? 'Q' : ' ');
        }
        out << '|' << endl;
    }
    out << endl << endl;
}

bool underAttack(bool **board, int side, int row, int col)
{
    static const int DIRECTIONS = 8;
    static const int DY[] = {-1,-1, 0, 1, 1, 1, 0,-1}; // N, NE, E, SE, S, SW, W, NW
    static const int DX[] = { 0, 1, 1, 1, 0,-1,-1,-1}; // N, NE, E, SE, S, SW, W, NW

    bool attack = false;

    // for each direction ...
    for (int dir = 0; dir < DIRECTIONS && !attack; ++dir) {

        // walk till finding a queen, or border
        int y = row + DY[dir];
        int x = col + DX[dir];
        while (0 <= y && y < side && 0 <= x && x < side && !attack) {

            // if a queen is found, the square is under attack
            attack = board[y][x];
            y += DY[dir];
            x += DX[dir];
        }
    }
    return attack;
}

bool placeQueens(bool **board, int side, int row)
{
    bool result = false;
    for (int col = 0; col < side && !result; ++col) {
        if (!underAttack(board, side, row, col)) {

            // this square is not attacked,
            // let's try to place a queen here
            board[row][col] = true;

            if (row == side-1) {
                // hey! this is the last row!
                result = true;
            } else {
                // otherwise, let's try to place
                // more queens in the following rows
                result = placeQueens(board, side, row+1);
            }

            // no luck this way, let's remove the queen
            // (backtracking)
            if (!result) board[row][col] = false;
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int side = 6;
    if (argc > 1) {
        istringstream arg1(argv[1]);
        arg1 >> side;
    }

    // allocation and initialization of board
    bool **board = new bool*[side];
    for (int y = 0; y < side; ++y) {
        board[y] = new bool[side];
        for (int x = 0; x < side; ++x) {
            board[y][x] = false;
        }
    }

    // solution: place queens starting from first row
    placeQueens(board, side, 0);
    printBoard(board, side, cout);

    // deallocate memory
    for (int y = 0; y < side; ++y) {
        delete[] board[y];
    }
    delete[] board;

    return 0;
}
