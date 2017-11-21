/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QGridLayout>
#include <QPushButton>
#include <QMessageBox>
#include "fifteengui.h"

FifteenGui::FifteenGui(FifteenPuzzle* puzzle)
{
    this->puzzle = puzzle;

    QGridLayout* layout = new QGridLayout();
    buttons = new QButtonGroup(this);
    for (int y = 0; y < puzzle->rows(); ++y) {
        for (int x = 0; x < puzzle->cols(); ++x) {
            QPushButton* b = new QPushButton();
            buttons->addButton(b, y * puzzle->cols() + x);
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();
    setLayout(layout);
    fixSize();

    connect(buttons, SIGNAL(buttonClicked(int)), this, SLOT(handleClick(int)));

    setWindowTitle(tr("Fifteen Puzzle"));
    show();
}

void FifteenGui::fixSize() {
    layout()->setMargin(0);
    layout()->setSpacing(0);
    layout()->setSizeConstraint(QLayout::SetFixedSize);
    adjustSize();
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < puzzle->rows(); y++) {
        for (int x = 0; x < puzzle->cols(); x++) {
            char symbol = puzzle->get(x, y);
            int i = y * puzzle->cols() + x;
            auto b = buttons->button(i);
            b->setText(QString(symbol));
            b->setEnabled(symbol != FifteenPuzzle::BLANK_SYMBOL);
        }
    }
}

void FifteenGui::handleClick(int i)
{
    int x = i % puzzle->cols();
    int y = i / puzzle->cols();
    puzzle->move(x, y);
    updateAllButtons();

    if (puzzle->isFinished()) {
        QMessageBox::information(this, tr("Congratulations"),
                                 tr("Game finished!"));
        puzzle->shuffle();
        updateAllButtons();
    }
}
