/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
