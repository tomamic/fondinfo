#include "tentspuzzle.h"

using namespace std;

TentsPuzzle::TentsPuzzle() {
}

void TentsPuzzle::place_tent(int x, int y) {
    if (get(x, y) == EMPTY) {
        board_[y * cols_ + x] = TENT;
    }
}

string TentsPuzzle::str() {
    return "";
}

bool TentsPuzzle::solved() {
    return false;
}

char TentsPuzzle::get(int x, int y) {
    if (0 <= x && x < cols_ && 0 <= y && y < rows_) {
        return board_[y * cols_ + x];
    }
    return OUT;
}

int TentsPuzzle::rows() {
    return rows_;
}

int TentsPuzzle::cols() {
    return cols_;
}

int TentsPuzzle::count_row(int y) {
    int tents = 0;
    for (int x = 0; x < cols_; ++x) {
        if (get(x, y) == TENT) ++tents;
    }
    return tents;
}

int TentsPuzzle::count_col(int x) {
    int tents = 0;
    for (int y = 0; y < rows_; ++y) {
        if (get(x, y) == TENT) ++tents;
    }
    return tents;
}

int TentsPuzzle::count_around(int x, int y) {
    int tents = 0;
    if (get(x, y - 1) == TENT) ++tents;      // up
    if (get(x + 1, y - 1) == TENT) ++tents;  // up-right
    if (get(x + 1, y) == TENT) ++tents;      // right
    if (get(x + 1, y + 1) == TENT) ++tents;  // down-right
    if (get(x, y + 1) == TENT) ++tents;      // down
    if (get(x - 1, y + 1) == TENT) ++tents;  // down-left
    if (get(x - 1, y) == TENT) ++tents;      // left
    if (get(x - 1, y - 1) == TENT) ++tents;  // up-left
    return tents;
}
