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

    auto layout = new QGridLayout();
    buttons = new QButtonGroup(this);
    for (int y = 0; y < puzzle->rows(); ++y) {
        for (int x = 0; x < puzzle->cols(); ++x) {
            auto b = new QPushButton();
            buttons->addButton(b, y * puzzle->cols() + x);
            layout->addWidget(b, y, x);
        }
    }
    updateAllButtons();
    setLayout(layout);
    fixAppearance();

    connect(buttons, SIGNAL(buttonClicked(int)), this, SLOT(handleClick(int)));
}

void FifteenGui::fixAppearance() {
    setWindowTitle(tr("Fifteen Puzzle"));
    layout()->setMargin(0);
    layout()->setSpacing(0);
    layout()->setSizeConstraint(QLayout::SetFixedSize);
    adjustSize();
    show();
}

void FifteenGui::updateAllButtons()
{
    for (int y = 0; y < puzzle->rows(); y++) {
        for (int x = 0; x < puzzle->cols(); x++) {
            auto symbol = puzzle->get(x, y);
            auto i = y * puzzle->cols() + x;
            auto b = buttons->button(i);
            b->setText(QString(symbol));
            b->setEnabled(symbol != FifteenPuzzle::BLANK_SYMBOL);
        }
    }
}

void FifteenGui::handleClick(int i)
{
    auto x = i % puzzle->cols();
    auto y = i / puzzle->cols();
    puzzle->move(x, y);
    updateAllButtons();

    if (puzzle->isFinished()) {
        QMessageBox::information(this, tr("Congratulations"),
                                 tr("Game finished!"));
        puzzle->shuffle();
        updateAllButtons();
    }
}
