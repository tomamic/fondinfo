/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FLOWERSGUI_H
#define FLOWERSGUI_H

#include "flowerspuzzle.h"
#include "rightbuttongroup.h"

#include <QtGui>

class FlowersGui : public QMainWindow
{
    Q_OBJECT

public:
    FlowersGui(FlowersPuzzle* puzzle);

private slots:
    void controlButtons(int i);
    void controlRightButtons(int i);
    void newGame();

private:
    void createButtons();
    void updateAllButtons();
    void checkSolution();

    RightButtonGroup* buttons;
    FlowersPuzzle* puzzle;
};

#endif // FLOWERSGUI_H
