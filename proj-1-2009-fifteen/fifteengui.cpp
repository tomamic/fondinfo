/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <QGridLayout>
#include <QPushButton>
#include <QMessageBox>
#include "fifteengui.h"

FifteenGui::FifteenGui(FifteenPuzzle* model)
{
    this->model = model;

    QGridLayout* layout = new QGridLayout();
    buttons = new QButtonGroup();
    for (int y = 0; y < model->getRows(); ++y) {
        for (int x = 0; x < model->getCols(); ++x) {
            QPushButton* b = new QPushButton();
            buttons->addButton(b, y * model->getCols() + x);
            layout->addWidget(b, y, x);
            // b->setStyleSheet("background: yellow");
        }
    }
    updateAllButtons();
    setLayout(layout);

    connect(buttons, SIGNAL(buttonClicked(int)),
            this, SLOT(controlButtons(int)));

    // setStyleSheet("background: green");
    setWindowTitle(tr("Fifteen Puzzle"));
    show();
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < model->getRows(); y++) {
        for (int x = 0; x < model->getCols(); x++) {
            char symbol = model->get(y, x);
            int i = y * model->getCols() + x;
            buttons->button(i)->setText(QString(symbol));
        }
    }
    checkSolution();
}

void FifteenGui::controlButtons(int i)
{
    int y = i / model->getCols();
    int x = i % model->getCols();

    model->move(y, x);
    updateAllButtons();
}

void FifteenGui::checkSolution()
{
    if (model->isSolved()) {
        QMessageBox::information(this, tr("Puzzle solved!"),
                                 tr("Puzzle solved!"));
        model->shuffle();
        updateAllButtons();
    }
}
