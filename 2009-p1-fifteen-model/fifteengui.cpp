/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteengui.h"

FifteenGui::FifteenGui(FifteenModel* model, QWidget* parent)
    : QWidget(parent)
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
            buttons->addButton(b, index({x, y}));
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();

    this->setLayout(layout);
    QObject::connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));
    // connection added for model signals
    QObject::connect(model, SIGNAL(blankMoved()),
                     this, SLOT(updateAfterMove()));
    show();
}

FifteenGui::~FifteenGui()
{
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < model->getRows(); y++) {
        for (int x = 0; x < model->getColumns(); x++) {
            buttons->button(index({x, y}))->setText(
                    QString(model->get({x, y})));
        }
    }
    checkSolution();
}

void FifteenGui::controlButtons(int i)
{
    int y = i / model->getColumns();
    int x = i % model->getColumns();

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

    checkSolution();
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

int FifteenGui::index(FifteenModel::Coord pos)
{
    return pos.imag() * model->getColumns() + pos.real();
}
