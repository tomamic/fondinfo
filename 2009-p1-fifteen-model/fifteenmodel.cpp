#include "fifteenmodel.h"

FifteenModel::FifteenModel(int rows, int columns)
    : shuffling(false), FifteenPuzzle(rows, columns)
{
}

void FifteenModel::shuffle()
{
    shuffling = true;
    FifteenPuzzle::shuffle();
    shuffling = false;
}

void FifteenModel::moveBlank(Coord delta)
{
    FifteenPuzzle::moveBlank(delta);
    if (!shuffling) emit blankMoved();
}

FifteenPuzzle::Coord FifteenModel::getBlank()
{
    return blank;
}

FifteenPuzzle::Coord FifteenModel::getMoved()
{
    return moved;
}
