#include "fifteenmodel.h"

FifteenModel::FifteenModel(int rows, int columns)
    : silent(false), FifteenPuzzle(rows, columns)
{
}

void FifteenModel::shuffle()
{
    silent = true;
    FifteenPuzzle::shuffle();
    silent = false;
}

void FifteenModel::moveBlank(Coord delta)
{
    FifteenPuzzle::moveBlank(delta);
    if (!silent) emit blankMoved();
}

FifteenPuzzle::Coord FifteenModel::getBlank()
{
    return blank;
}

FifteenPuzzle::Coord FifteenModel::getMoved()
{
    return moved;
}
