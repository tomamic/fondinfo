/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

void zigzag(vector< vector<int> > & matrix) {
    int rows = matrix.size();
    int columns = matrix[0].size();

    // initially: bottom-left cell, heading down-right
    int y = rows - 1, x = 0;
    int dy = +1, dx = +1;

    for (int i = 0; i < rows * columns; ++i) {
        matrix[y][x] = i;

        y += dy; x += dx;

        // if out of bounds...
        if (y < 0 || rows <= y || x < 0 || columns <= x) {
            // invert direction and go one step back
            dy = -dy; dx = -dx;
            y += dy; x += dx;

            // shift along the border by one
            if (x == columns - 1) --y;
            else if (y == rows - 1) ++x;
            else if (y == 0) ++x;
            else if (x == 0) --y;
        }
    }
}

int main(int argc, char *argv[])
{
    int rows = 0, columns = 0;
    while (rows <= 0 || columns <= 0) {
        cout << "Rows, columns?" << endl;
        cin >> rows >> columns;
    }

    vector< vector<int> > matrix(rows, vector<int>(columns));
    zigzag(matrix);

    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < columns; ++x) {
            cout << setw(4) << matrix[y][x];
        }
        cout << endl;
    }

    return 0;
}
