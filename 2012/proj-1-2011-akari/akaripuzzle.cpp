/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "akaripuzzle.h"

#include <iomanip>

using namespace std;

AkariPuzzle::AkariPuzzle()
{
    rows = 0;
    columns = 0;
}

void AkariPuzzle::read(istream& in)
{
    // *add* cleanup code here
    in >> noskipws;
    char c;
    while (in >> c) {
        if (c != '\n') { table.push_back(c); }
        else if (columns == 0) { columns = table.size(); }
    }
    rows = table.size() / columns;
}

void AkariPuzzle::write(ostream& out)
{
    for (int i = 0; i < table.size(); ++i) {
        out << table[i];
        if (i % columns == columns - 1) out << endl;
    }
    out << endl;
}

char AkariPuzzle::get(int y, int x)
{
    char c = OUT_OF_BOUNDS;
    if (0 <= y && y < rows && 0 <= x && x < columns) {
        c = table[y * columns + x];
    }
    return c;
}

void AkariPuzzle::set(int y, int x, char val)
{
    table[y * columns + x] = val;
}

void AkariPuzzle::putBulb(int y, int x)
{
    if (get(y, x) == EMPTY) {
        set(y, x, BULB);
        illuminate(y, x, -1, 0); // UP
        illuminate(y, x, 0, +1); // RIGHT
        illuminate(y, x, +1, 0); // DOWN
        illuminate(y, x, 0, -1); // LEFT
    }
}

void AkariPuzzle::illuminate(int y, int x, int dy, int dx)
{
    int y1 = y + dy;
    int x1 = x + dx;
    while (get(y1, x1) == EMPTY || get(y1, x1) == LIGHT) {
        set(y1, x1, LIGHT);
        y1 += dy;
        x1 += dx;
    }
}

bool AkariPuzzle::checkConstraint(int y, int x)
{
    int missingBulbs = get(y, x) - WALL0; // how many bulbs have to be placed around?
    if (get(y - 1, x) == BULB) { --missingBulbs; } // UP
    if (get(y, x + 1) == BULB) { --missingBulbs; } // RIGHT
    if (get(y + 1, x) == BULB) { --missingBulbs; } // DOWN
    if (get(y, x - 1) == BULB) { --missingBulbs; } // LEFT

    // *add* code here to count free cells, too

    return 0 <= missingBulbs; // && missingBulbs <= freeCells
}
