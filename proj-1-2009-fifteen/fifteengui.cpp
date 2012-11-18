/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QGridLayout>
#include <QPushButton>
#include <QMessageBox>
#include "fifteengui.h"

FifteenGui::FifteenGui(FifteenPuzzle* game)
{
    this->game = game;

    QGridLayout* layout = new QGridLayout();
    buttons = new QButtonGroup();
    for (int y = 0; y < game->getRows(); ++y) {
        for (int x = 0; x < game->getCols(); ++x) {
            QPushButton* b = new QPushButton();
            buttons->addButton(b, y * game->getCols() + x);
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
    for (int y = 0; y < game->getRows(); y++) {
        for (int x = 0; x < game->getCols(); x++) {
            char symbol = game->get(y, x);
            int i = y * game->getCols() + x;
            buttons->button(i)->setText(QString(symbol));
        }
    }
    checkFinished();
}

void FifteenGui::controlButtons(int i)
{
    int y = i / game->getCols();
    int x = i % game->getCols();

    game->move(y, x);
    updateAllButtons();
}

void FifteenGui::checkFinished()
{
    if (game->isFinished()) {
        QMessageBox::information(
                    this, tr("Game finished!"), tr("Game finished!"));
        game->shuffle();
        updateAllButtons();
    }
}
