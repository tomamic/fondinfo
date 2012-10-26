/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "board.h"

// N, NE, E, SE, S, SW, W, NW
const int Board::DY[] = {-1,-1, 0, 1, 1, 1, 0,-1};
const int Board::DX[] = { 0, 1, 1, 1, 0,-1,-1,-1};

using namespace std;

Board::Board(int height, int width)
{
    this->height = height;
    this->width = width;
    board.assign(height, vector<bool>(width, false));
}

bool Board::solve()
{
    return placeQueens(0);
}

void Board::write(ostream &out)
{
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            if (board[y][x]) {
                out << "|Q";
            } else {
                out << "| ";
            }
        }
        out << '|' << endl;
    }
    out << endl << endl;
}

bool Board::underAttack(int row, int col)
{
    bool attack = false;
    // for each direction ...
    for (int dir = 0; dir < DIRECTIONS && !attack; ++dir) {
        int y = row + DY[dir];
        int x = col + DX[dir];
        // walk till finding a queen, or border
        while (0 <= y && y < height && 0 <= x
               && x < width && !attack) {
            // if a queen is found, the square is under attack
            attack = board[y][x];
            y += DY[dir];
            x += DX[dir];
        }
    }
    return attack;
}

bool Board::placeQueens(int row)
{
    bool result = false;
    for (int col = 0; col < width && !result; ++col) {
        if (!underAttack(row, col)) {

            // this square is not attacked,
            // let's try to place a queen here
            board[row][col] = true;
            if (row == height - 1) {
                // hey! this is the last row!
                result = true;
            } else {
                // otherwise, let's try to place
                // more queens in the following rows
                result = placeQueens(row+1);
            }

            // no luck this way, let's remove the queen
            // (backtracking)
            if (!result) {
                board[row][col] = false;
            }
        }
    }
    return result;
}
