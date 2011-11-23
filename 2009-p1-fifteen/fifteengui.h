#ifndef FIFTEENGUI_H
#define FIFTEENGUI_H

#include "fifteenpuzzle.h"

#include <QtGui>

class FifteenGui : public QWidget {
    Q_OBJECT

public:
    FifteenGui(FifteenPuzzle* model, QWidget* parent = NULL);
    ~FifteenGui();

public slots:
    void controlButtons(int i);

private:
    void updateAllButtons();
    void checkSolution();

    QButtonGroup* buttons;
    FifteenPuzzle* model;
};

#endif // FIFTEENGUI_H
