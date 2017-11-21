/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "memory.h"

#include <vector>
#include <algorithm>

using namespace std;

Memory::Memory(int rows, int cols)
{
    this->rows = rows;
    this->cols = cols;
    move1 = -1;
    move2 = -1;
    matrix.assign(rows * cols, 0);

    sort();
    shuffle();
}

void Memory::sort()
{
    for (int i = 0; i < matrix.size(); ++i) {
        matrix[i] = FIRST_HIDDEN + i/2;
    }
}

void Memory::shuffle()
{
//    random_shuffle(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        int j = rand() % matrix.size();
        int temp = matrix[i];
        matrix[i] = matrix[j];
        matrix[j] = temp;
    }
}

void Memory::uncover(int card1, int card2) {
    if (card1 != card2
            && 0 <= card1 && card1 < matrix.size()
            && 0 <= card2 && card2 < matrix.size()) {
        move1 = card1;
        move2 = card2;
        if (matrix[card1] == matrix[card2]) {
            matrix[card1] += FIRST - FIRST_HIDDEN;
            matrix[card2] += FIRST - FIRST_HIDDEN;
        }
    }
}

bool Memory::isFinished() {
    bool ok = true;
    for (int i = 0; i < matrix.size() && ok; ++i) {
        ok = (FIRST <= matrix[i] && matrix[i] <= LAST);
    }
    return ok;
}

void Memory::write(ostream &out) {
    for (int i = 0; i < matrix.size(); ++i) {
        char c = matrix[i];
        if (FIRST <= c && c <= LAST) {
            out << c;
        } else if (i == move1 || i == move2) {
            out << char(c + FIRST - FIRST_HIDDEN);
        } else {
            out << JOLLY;
        }
        if (i % cols == cols - 1) out << endl;
    }
    out << endl;
}
