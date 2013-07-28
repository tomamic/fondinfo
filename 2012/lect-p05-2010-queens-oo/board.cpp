/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "board.h"

#include <sstream>

using namespace std;

Board::Board(int side)
{
    this->side = side;
    board.assign(side * side, false);
}

bool Board::solve()
{
    return placeQueens(0);
}

void Board::write(ostream &out)
{
    const string ENDROW = "|\n";
    const string QUEEN = "|Q";
    const string EMPTY = "| ";

    for (int y = 0; y < side; ++y) {
        for (int x = 0; x < side; ++x) {
            if (board[y * side + x]) out << QUEEN;
            else out << EMPTY;
        }
        out << ENDROW;
    }
    out << endl;
}

string Board::__str__()
{
    ostringstream result;
    write(result);
    return result.str();
}

bool Board::underAttack(int row, int col)
{
    // for each direction up-left, up, up-right...
    // (there are no queens in lower cells)
    auto dy = -1;
    for (auto dx : {-1, 0, +1}) {
        auto y = row + dy;
        auto x = col + dx;

        // walk till finding a queen, or border
        while (0 <= y && y < side && 0 <= x && x < side) {

            // if a queen is found, the square is under attack
            if (board[y * side + x]) return true;
            y += dy;
            x += dx;
        }
    }
    return false;
}

bool Board::placeQueens(int row)
{
    for (auto col = 0; col < side; ++col) {
        if (!underAttack(row, col)) {

            // this square is not attacked,
            // let's try to place a queen here
            board[row *side + col] = true;
            if (row == side - 1) {
                // hey! this is the last row!
                return true;
            } 
            if (placeQueens(row + 1)) {
                // otherwise, let's try to place
                // more queens in the following rows
                return true;
            }

            // no luck this way, let's remove the queen
            // (backtracking)
            board[row * side + col] = false;
        }
    }
    return false;
}

