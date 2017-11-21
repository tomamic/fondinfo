/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

// const int NUM_DIRS = 4;
// const int DY[] = {-1,  0, +1,  0};
// const int DX[] = { 0, +1,  0, -1};

const int EMPTY = -1;

bool empty(const vector<vector<int> > & matrix, int y, int x)
{
    bool result = false;
    if (y >= 0 && y < matrix.size()
            && x >= 0 && x < matrix[y].size()) {
        result = (matrix[y][x] == EMPTY);
    }
    return result;
}

int main()
{
    int rows; cout << "rows? "; cin >> rows;
    int columns; cout << "columns? "; cin >> columns;
    vector<vector<int> > matrix(rows, vector<int>(columns, EMPTY));

    // initially: bottom-left cell, heading up
    int y = rows - 1, x = 0;
    int dy = -1, dx = 0;

    for (int i = 0; i < rows * columns; ++i) {
        matrix[y][x] = i;
        // advance
        y += dy; x += dx;
        // bounce against border or visited cell?
        if (!empty(matrix, y, x)) {
            // go one step back
            y -= dy; x -= dx;
            // turn clockwise
            int tmp = dy; dy = dx; dx = -tmp;
            // advance in new direction
            y += dy; x += dx;
        }
    }

    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < columns; ++x) {
            cout << setw(4) << matrix[y][x];
        }
        cout << endl;
    }
    return 0;
}
