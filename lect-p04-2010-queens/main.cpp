/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <vector>

using namespace std;

void printBoard(vector<vector<bool> > &board, ostream &out)
{
    const char SEPARATOR = '|';
    const char QUEEN = 'Q';
    const char EMPTY = ' ';

    for (int y = 0; y < board.size(); ++y) {
        for (int x = 0; x < board[y].size(); ++x) {
            cout << SEPARATOR;
            if (board[y][x]) {
                out << QUEEN;
            } else {
                out << EMPTY;
            }
        }
        out << SEPARATOR << endl;
    }
    out << endl;
}

bool underAttack(vector<vector<bool> >& board, int row, int col)
{
    bool attack = false;

    // for each direction up-left, up, up-right...
    // (there are no queens in lower cells)
    int dy = -1;
    for (int dx = -1; dx <= +1 && !attack; ++dx) {

        // walk till finding a queen, or border
        int y = row + dy;
        int x = col + dx;
        while (0 <= y && y < board.size() && 0 <= x && x < board[y].size() && !attack) {

            // if a queen is found, the square is under attack
            attack = board[y][x];
            y += dy;
            x += dx;
        }
    }
    return attack;
}

bool placeQueens(vector<vector<bool> >& board, int row)
{
    bool result = false;
    for (int col = 0; col < board[row].size() && !result; ++col) {
        if (!underAttack(board, row, col)) {

            // this square is not attacked,
            // let's try to place a queen here
            board[row][col] = true;
            if (row == board.size() - 1) {
                // hey! this is the last row!
                result = true;
            } else {
                // otherwise, let's try to place
                // more queens in the following rows
                result = placeQueens(board, row+1);
            }
            if (!result) {
                // no luck this way, let's remove the queen
                // (backtracking)
                board[row][col] = false;
            }
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int side;
    cout << "side? ";
    cin >> side;

    // allocation and initialization of board
    vector<vector<bool> > board(side, vector<bool> (side, false));

    // solution: place queens starting from first row
    placeQueens(board, 0);
    printBoard(board, cout);

    return 0;
}
