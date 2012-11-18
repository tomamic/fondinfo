/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
