/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "flowersgui.h"
#include "rightpushbutton.h"

FlowersGui::FlowersGui(FlowersPuzzle* puzzle)
{
    this->puzzle = puzzle;
    setWindowTitle(tr("Flowers Puzzle"));
    setStyleSheet("background: green");
    createLayout();
    show();
}

void FlowersGui::createLayout()
{
    if (centralWidget() != NULL) {
        delete centralWidget();
    }
    setCentralWidget(new QWidget());
    buttons = new RightButtonGroup(centralWidget());
    QGridLayout* layout = new QGridLayout();

    for (int y = 0; y < puzzle->getRows(); ++y) {
        for (int x = 0; x < puzzle->getColumns(); ++x) {
            RightPushButton *b = new RightPushButton();
            b->setStyleSheet("background: yellow");
            buttons->addButton(b, y * puzzle->getColumns() + x);
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();
    centralWidget()->setLayout(layout);

    connect(buttons, SIGNAL(buttonClicked(int)),
                     this, SLOT(controlButtons(int)));
    connect(buttons, SIGNAL(buttonRightClicked(int)),
                     this, SLOT(controlRightButtons(int)));
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
