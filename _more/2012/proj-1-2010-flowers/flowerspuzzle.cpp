/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "flowerspuzzle.h"
#include <cstdlib>
#include <vector>

using namespace std;

FlowersPuzzle::FlowersPuzzle(int rows, int cols, int flowers)
{
    create(rows, cols, flowers);
}

void FlowersPuzzle::create(int rows, int cols, int flowers)
{
    this->rows = rows;
    this->cols = cols;
    this->flowers = flowers;
    create();
}

void FlowersPuzzle::create()
{
    map.assign(rows, vector<char>(cols, ZERO));
    view.assign(rows, vector<char>(cols, UNKNOWN));

    for (int f = 0; f < flowers;) {
        int ry = rand() % rows;
        int rx = rand() % cols;
        if (getMap(ry, rx) != FLOWER) {
            setMap(ry, rx, FLOWER);
            ++f;
        }
    }
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < cols; ++x) {
            if (getMap(y, x) != FLOWER) {
                setMap(y, x, ZERO + countFlowers(y, x));
            }
        }
    }
    uncovered = 0;
    flagged = 0;
    lastX = -1;
    lastY = -1;
}

void FlowersPuzzle::setMap(int y, int x, int val)
{
    map[y][x] = val;
}

void FlowersPuzzle::setView(int y, int x, int val)
{
    view[y][x] = val;
    if (val != FLAG && val != UNKNOWN) ++uncovered;
}

int FlowersPuzzle::getRows()
{
    return rows;
}

int FlowersPuzzle::getCols()
{
    return cols;
}

char FlowersPuzzle::getMap(int y, int x)
{
    int val = OUT_OF_BOUNDS;
    if (0 <= x && x < cols && 0 <= y && y < rows) {
        val = map[y][x];
    }
    return val;
}

char FlowersPuzzle::getView(int y, int x)
{
    int val = OUT_OF_BOUNDS;
    if (0 <= x && x < cols && 0 <= y && y < rows) {
        val = view[y][x];
    }
    return val;
}

void FlowersPuzzle::flag(int y, int x)
{
    char c = getView(y, x);
    if (c == UNKNOWN) { setView(y, x, FLAG); ++flagged; }
    else if (c == FLAG) { setView(y, x, UNKNOWN); --flagged; }

    if (flagged == flowers) {
        for (int y = 0; y < rows; ++y) {
            for (int x = 0; x < cols; ++x) {
                if (getView(y, x) == UNKNOWN) {
                    uncover(y, x);
                }
            }
        }
    }
}

bool FlowersPuzzle::isWon()
{
    return uncovered == cols * rows - flowers;
}

bool FlowersPuzzle::isLost()
{
    return lastY >= 0 && lastX >= 0 && getMap(lastY, lastX) == FLOWER;
}

void FlowersPuzzle::uncover(int y, int x)
{
    char view0 = getView(y, x);
    if (view0 == UNKNOWN && !isWon() && !isLost()) {
        lastY = y;
        lastX = x;
        char map0 = getMap(y, x);
        setView(y, x, map0);
        if (map0 == ZERO) {
            uncoverAround(y, x);
        }
    }
}

void FlowersPuzzle::uncoverAround(int y, int x)
{
    for (int dy = -1; dy  <= +1; dy++) {
        for (int dx = -1; dx  <= +1; dx++) {
            if (dx != 0 || dy != 0) {
                int y1 = y+dy;
                int x1 = x+dx;
                uncover(y1, x1);
            }
        }
    }
}

int FlowersPuzzle::countFlowers(int y, int x)
{
    int result = 0;
    for (int dy = -1; dy  <= +1; dy++) {
        for (int dx = -1; dx  <= +1; dx++) {
            if (dx != 0 || dy != 0) {
                int y1 = y+dy;
                int x1 = x+dx;
                if (getMap(y1, x1) == FLOWER) {
                    ++result;
                }
            }
        }
    }
    return result;
}

void FlowersPuzzle::write(ostream& out)  {
    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {
            out << view[y][x];
        }
        cout << endl;
    }
}

