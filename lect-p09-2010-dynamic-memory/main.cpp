/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <sstream>

using namespace std;

void printBoard(bool** board, int side, ostream &out)
{
    for (int y = 0; y < side; ++y) {
        for (int x = 0; x < side; ++x) {
            if (board[y][x]) {
                cout << "|Q";
            } else {
                cout << "| ";
            }
        }
        out << '|' << endl;
    }
    out << endl;
}

bool underAttack(bool **board, int side, int row, int col)
{
    bool attack = false;

    // for each direction up-left, up, up-right...
    // (there are no queens in lower cells)
    int dy = -1;
    for (int dx = -1; dx <= +1 && !attack; ++dx) {

        // walk till finding a queen, or border
        int y = row + dy;
        int x = col + dx;
        while (0 <= y && y < side && 0 <= x && x < side && !attack) {

            // if a queen is found, the square is under attack
            attack = board[y][x];
            y += dy;
            x += dx;
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
        // get side as a command line argument
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
