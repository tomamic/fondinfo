/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef FIFTEENGUI_H
#define FIFTEENGUI_H

#include "fifteenmodel.h"

#include <QWidget>
#include <QButtonGroup>

class FifteenGui : public QWidget {
    Q_OBJECT

public:
    FifteenGui(FifteenModel* model);

private slots:
    // method added for model signals
   void updateAfterMove();
    void controlButtons(int i);

private:
    void updateAllButtons();
    void checkFinished();
    int index(FifteenPuzzle::Coord pos);

    QButtonGroup* buttons;
    FifteenModel* model;
};

#endif // FIFTEENGUI_H
