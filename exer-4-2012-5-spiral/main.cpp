#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

const int DY = 0, DX = 1;
const vector< vector<int> > DIRECTIONS = {
    {-1, 0}, {0, +1}, {+1, 0}, {0, -1}};

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
    int d = 0;
    int dy = DIRECTIONS[d][DY], dx = DIRECTIONS[d][DX];

    for (int i = 0; i < rows * columns; ++i) {
        matrix[y][x] = i;
        // advance
        y += dy; x += dx;
        // bounce against border or visited cell?
        if (!empty(matrix, y, x)) {
            // go one step back
            y -= dy; x -= dx;
            // turn clockwise
            //int tmp = dy; dy = dx; dx = -tmp;
            d = (d + 1) % DIRECTIONS.size();
            dy = DIRECTIONS[d][DY];
            dx = DIRECTIONS[d][DX];
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
