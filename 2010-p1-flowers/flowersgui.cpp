/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "flowersgui.h"
#include "rightpushbutton.h"

FlowersGui::FlowersGui(FlowersPuzzle* model, QWidget* parent) : QWidget(parent)
{
    this->puzzle = model;
    setWindowTitle(tr("Flowers Puzzle"));
    setStyleSheet("background: green");
    QGridLayout* layout = new QGridLayout();
    buttons = new RightButtonGroup();
    for (int y = 0; y < model->getRows(); ++y) {
        for (int x = 0; x < model->getColumns(); ++x) {
            RightPushButton *b = new RightPushButton();
            b->setStyleSheet("background: yellow");
            buttons->addButton(b, y * model->getColumns() + x);
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();

    this->setLayout(layout);
    QObject::connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));
    QObject::connect(buttons, SIGNAL(buttonRightClicked(int)),
                     this, SLOT(controlRightButtons(int)));
    show();
}

FlowersGui::~FlowersGui()
{
}

void FlowersGui::updateAllButtons()
{
    for (int y = 0; y < puzzle->getRows(); y++) {
        for (int x = 0; x < puzzle->getColumns(); x++) {
            char symbol = puzzle->getView(y, x);
            int i = y * puzzle->getColumns() + x;
            buttons->button(i)->setText(QString(symbol));
        }
    }
    checkSolution();
}

void FlowersGui::controlButtons(int i)
{
    int y = i / puzzle->getColumns();
    int x = i % puzzle->getColumns();
    puzzle->uncover(y, x);
    updateAllButtons();
}

void FlowersGui::controlRightButtons(int i)
{
    int y = i / puzzle->getColumns();
    int x = i % puzzle->getColumns();
    puzzle->flag(y, x);
    updateAllButtons();
}

void FlowersGui::checkSolution()
{
    if (puzzle->isWon()) {
        QMessageBox::information(this, tr("Puzzle solved!"), tr("Puzzle solved!"));
        puzzle->shuffle();
        updateAllButtons();
    } else if (puzzle->isLost()) {
        QMessageBox::information(this, tr("Game lost!"), tr("Game lost!"));
        puzzle->shuffle();
        updateAllButtons();
    }
}
