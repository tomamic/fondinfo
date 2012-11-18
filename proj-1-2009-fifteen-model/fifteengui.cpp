/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteengui.h"
#include <QGridLayout>
#include <QPushButton>
#include <QMessageBox>

FifteenGui::FifteenGui(FifteenModel* model)
{
    this->model = model;

    QGridLayout* layout = new QGridLayout();
    buttons = new QButtonGroup();
    for (int y = 0; y < model->getRows(); ++y) {
        for (int x = 0; x < model->getCols(); ++x) {
            QPushButton* b = new QPushButton();
            buttons->addButton(b, index({x, y}));
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();
    setLayout(layout);

    // connection added for model signals
    connect(model, SIGNAL(blankMoved()),
                     this, SLOT(updateAfterMove()));
    connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));

    setWindowTitle(tr("Fifteen Puzzle"));
    show();
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < model->getRows(); y++) {
        for (int x = 0; x < model->getCols(); x++) {
            buttons->button(index({x, y}))->setText(
                    QString(model->get({x, y})));
        }
    }
    checkFinished();
}

void FifteenGui::controlButtons(int i)
{
    int y = i / model->getCols();
    int x = i % model->getCols();

    model->move({x, y});
    // call removed for model signals
    // updateAllButtons();
}

void FifteenGui::updateAfterMove()
{
    FifteenModel::Coord moved = model->getMoved();
    buttons->button(index(moved))->setText(
                QString(model->get(moved)));

    FifteenModel::Coord blank = model->getBlank();
    buttons->button(index(blank))->setText(
                QString(model->get(blank)));

    checkFinished();
}

void FifteenGui::checkFinished()
{
    if (model->isFinished()) {
        QMessageBox::information(
                    this, tr("Game finished!"), tr("Game finished!"));
        model->shuffle();
        updateAllButtons();
    }
}

int FifteenGui::index(FifteenModel::Coord pos)
{
    return pos.imag() * model->getCols() + pos.real();
}
