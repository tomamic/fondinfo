/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "sea.h"

const int DIRS = 4;
const int DY[] = {-1,  0, +1,  0};
const int DX[] = { 0, +1,  0, -1};

Sea::Sea(int rows, int cols)
{
    this->rows = rows;
    this->cols = cols;
    matrix.assign(rows, vector<bool>(cols, false));
}

bool Sea::place(int y, int x, int dir, int size)
{
    bool result = (0 <= y && y < rows
                   && 0 <= x && x < cols
                   && !matrix[y][x]);

    if (result && size > 1) {
        result = place(y + DY[dir], x + DX[dir], dir, size - 1);
    }
    if (result) {
        matrix[y][x] = true;
    }
    return result;
}

void Sea::print(ostream &out)
{
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < cols; ++x) {
            cout << matrix[y][x];
        }
        out << endl;
    }
    out << endl;
}

int Sea::getRows()
{
    return rows;
}

int Sea::getCols()
{
    return rows;
}

int Sea::getDirs()
{
    return DIRS;
}
