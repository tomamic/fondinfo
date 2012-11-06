/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteengui.h"

FifteenGui::FifteenGui(FifteenPuzzle* model, QWidget* parent) : QWidget(parent)
{
    this->model = model;
    setWindowTitle(tr("Fifteen Puzzle"));
    setStyleSheet("background: green");
    QGridLayout* layout = new QGridLayout();
    buttons = new QButtonGroup();
    for (int y = 0; y < model->getRows(); ++y) {
        for (int x = 0; x < model->getColumns(); ++x) {
            QPushButton *b = new QPushButton();
            b->setStyleSheet("background: yellow");
            buttons->addButton(b, y * model->getColumns() + x);
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();

    this->setLayout(layout);
    QObject::connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));
    show();
}

FifteenGui::~FifteenGui()
{
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < model->getRows(); y++) {
        for (int x = 0; x < model->getColumns(); x++) {
            char symbol = model->get(y, x);
            int i = y * model->getColumns() + x;
            buttons->button(i)->setText(QString(symbol));
        }
    }
    checkSolution();
}

void FifteenGui::controlButtons(int i)
{
    int y = i / model->getColumns();
    int x = i % model->getColumns();

    model->move(y, x);
    updateAllButtons();
}

void FifteenGui::checkSolution()
{
    if (model->isSolved()) {
        QMessageBox::information(this, tr("Puzzle solved!"), tr("Puzzle solved!"));
        model->shuffle();
        updateAllButtons();
    }
}
