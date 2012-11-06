/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef FLOWERSGUI_H
#define FLOWERSGUI_H

#include "flowerspuzzle.h"
#include "rightbuttongroup.h"

#include <QtGui>

class FlowersGui : public QWidget
{
    Q_OBJECT

public:
    FlowersGui(FlowersPuzzle* puzzle, QWidget* parent = NULL);
    ~FlowersGui();

public slots:
    void controlButtons(int i);
    void controlRightButtons(int i);

private:
    void updateAllButtons();
    void checkSolution();

    RightButtonGroup* buttons;
    FlowersPuzzle* puzzle;
};

#endif // FLOWERSGUI_H
