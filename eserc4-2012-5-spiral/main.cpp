#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

const int EMPTY = -1;
const int OUT = -2;

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

    int y = rows - 1;
    int x = 0;
    int dy = -1;
    int dx = 0;
    int i = 0;

    while (empty(matrix, y, x)) {
        matrix[y][x] = i;
        ++i;
        // advance
        y += dy;
        x += dx;
        // bounce against border or visited cell?
        if (!empty(matrix, y, x)) {
            // go one step back
            y -= dy;
            x -= dx;
            // turn clockwise
            int tmp = dy;
            dy = dx;
            dx = -tmp;
            // advance in new direction
            y += dy;
            x += dx;
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
