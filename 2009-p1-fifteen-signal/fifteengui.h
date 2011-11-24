/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef FIFTEENGUI_H
#define FIFTEENGUI_H

#include "fifteenpuzzle.h"
#include "rightbuttongroup.h"

#include <QtGui>

class FifteenGui : public QWidget {
    Q_OBJECT

public:
    FifteenGui(FifteenPuzzle* model, QWidget* parent = NULL);
    ~FifteenGui();

public slots:
    void controlButtons(int i);
     // method added for model signals
    void updateAfterMove(int newY, int newX, int oldY, int oldX);

private:
    void updateAllButtons();
    void checkSolution();

    RightButtonGroup* buttons;
    FifteenPuzzle* model;
};

#endif // FIFTEENGUI_H
