/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "flowersgui.h"
#include "rightpushbutton.h"
#include <iostream>

FlowersGui::FlowersGui(FlowersPuzzle* puzzle)
{
    this->puzzle = puzzle;

    setWindowTitle(tr("Flowers Puzzle"));
    createButtons();

    QMenu* menu = menuBar()->addMenu(tr("Game"));
    QAction* newAction = menu->addAction("New...");
    connect(newAction, SIGNAL(triggered()), this, SLOT(newGame()));
    show();
}

void FlowersGui::createButtons()
{
    if (centralWidget() != NULL) {
        delete centralWidget();
    }
    setCentralWidget(new QWidget());

    buttons = new RightButtonGroup(centralWidget());
    QGridLayout* layout = new QGridLayout();

    for (int y = 0; y < puzzle->getRows(); ++y) {
        for (int x = 0; x < puzzle->getCols(); ++x) {
            RightPushButton *b = new RightPushButton();
            b->setStyleSheet("background: yellow");
            b->setFixedSize(20, 20);
            buttons->addButton(b, y * puzzle->getCols() + x);
            layout->addWidget(b, y, x);
        }
    }
    layout->setSpacing(0);
    layout->setSizeConstraint(QLayout::SetFixedSize);
    centralWidget()->setLayout(layout);
    centralWidget()->setStyleSheet("background: green");
    updateAllButtons();
    adjustSize();

    connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));
    connect(buttons, SIGNAL(buttonRightClicked(int)),
                     this, SLOT(controlRightButtons(int)));
}

void FlowersGui::updateAllButtons()
{
    for (int y = 0; y < puzzle->getRows(); y++) {
        for (int x = 0; x < puzzle->getCols(); x++) {
            char symbol = puzzle->getView(y, x);
            int i = y * puzzle->getCols() + x;
            buttons->button(i)->setText(QString(symbol));
        }
    }
    checkSolution();
}

void FlowersGui::controlButtons(int i)
{
    int y = i / puzzle->getCols();
    int x = i % puzzle->getCols();
    puzzle->uncover(y, x);
    updateAllButtons();
}

void FlowersGui::controlRightButtons(int i)
{
    int y = i / puzzle->getCols();
    int x = i % puzzle->getCols();
    puzzle->flag(y, x);
    updateAllButtons();
}

void FlowersGui::newGame()
{
    int rows = QInputDialog::getInt(this, "Rows?", "Rows?", 9, 5, 25);
    int cols = QInputDialog::getInt(this, "Cols?", "Cols?", 9, 5, 25);
    int flowers = QInputDialog::getInt(this, "Flowers?", "Flowers?", 10, 5, 25);
    puzzle->create(rows, cols, flowers);
    createButtons();
}

void FlowersGui::checkSolution()
{
    if (puzzle->isWon()) {
        QMessageBox::information(this, tr("Puzzle solved!"), tr("Puzzle solved!"));
        puzzle->create();
        updateAllButtons();
    } else if (puzzle->isLost()) {
        QMessageBox::information(this, tr("Game lost!"), tr("Game lost!"));
        puzzle->create();
        updateAllButtons();
    }
}
