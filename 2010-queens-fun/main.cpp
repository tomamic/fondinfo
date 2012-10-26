/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <vector>

using namespace std;

void printBoard(vector<vector<bool> > &board, ostream &out)
{
    for (int y = 0; y < board.size(); ++y) {
        for (int x = 0; x < board[y].size(); ++x) {
            if (board[y][x]) {
                out << "|Q";
            } else {
                out << "|-";
            }
        }
        out << "|" << endl;
    }
    out << endl << endl;
}

bool underAttack(vector<vector<bool> >& board, int row, int col)
{
    static const int DIRECTIONS = 8;
    static const int DY[] = {-1,-1, 0, 1, 1, 1, 0,-1}; // N, NE, E, SE, S, SW, W, NW
    static const int DX[] = { 0, 1, 1, 1, 0,-1,-1,-1}; // N, NE, E, SE, S, SW, W, NW

    bool attack = false;
    for (int dir = 0; dir < DIRECTIONS && !attack; ++dir) {
        int y = row + DY[dir];
        int x = col + DX[dir];
        while (0 <= y && y < board.size() && 0 <= x && x < board[y].size() && !attack) {
            attack = board[y][x];
            y += DY[dir];
            x += DX[dir];
        }
    }
    return attack;
}

bool placeQueens(vector<vector<bool> >& board, int row)
{
    bool result = false;
    for (int col = 0; col < board[row].size() && !result; ++col) {
        if (!underAttack(board, row, col)) {
            board[row][col] = true;
            if (row == board.size() - 1) {
                result = true;
            } else {
                result = placeQueens(board, row+1);
            }
            if (!result) {
                board[row][col] = false; // backtracking
            }
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int side;
    cin >> side;

    vector<vector<bool> > board(side, vector<bool> (side, false));

    placeQueens(board, 0);
    printBoard(board, cout);

    return 0;
}
