/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEENMODEL_H
#define FIFTEENMODEL_H

#include <QObject>
#include "fifteenpuzzle.h"

class FifteenModel
        : public QObject, public FifteenPuzzle
{
    Q_OBJECT

public:
    FifteenModel(int rows, int cols);
    void shuffle();
    Coord getBlank();
    Coord getMoved();

signals:
    void blankMoved();

protected:
    void moveBlank(Coord delta);
    bool silent = false;
};

#endif // FIFTEENMODEL_H
