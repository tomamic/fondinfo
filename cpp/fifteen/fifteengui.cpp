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
    this->puzzle_ = puzzle;

    auto grid = new QGridLayout; setLayout(grid);
    for (auto y = 0; y < rows(); ++y) {
        for (auto x = 0; x < cols(); ++x) {
            auto b = new QPushButton;
            buttons_.push_back(b);
            grid->addWidget(b, y, x);
            connect(b, &QPushButton::clicked,
                    [=]{ handle_click(x, y); });
        }
    }
    fix_appearance();
    update_all_buttons();
}

void FifteenGui::fix_appearance() {
    setWindowTitle(tr("Fifteen Puzzle"));
    layout()->setMargin(0);
    layout()->setSpacing(0);
    layout()->setSizeConstraint(QLayout::SetFixedSize);
    adjustSize();
    show();
}

void FifteenGui::update_button(int x, int y) {
    auto val = puzzle_->get({x, y});
    auto symbol = 'A' + val - FifteenPuzzle::FIRST;
    if (val == FifteenPuzzle::BLANK) symbol = ' ';

    auto b = buttons_[y * cols() + x];
    b->setText(QString{symbol});
}

void FifteenGui::update_all_buttons() {
    for (auto y = 0; y < rows(); y++)
        for (auto x = 0; x < cols(); x++)
            update_button(x, y);
}

void FifteenGui::handle_click(int x, int y)
{
    puzzle_->move({x, y});
    for (auto cell : {puzzle_->blank(), puzzle_->moved()}) {
        update_button(cell.real(), cell.imag());
    }

    if (puzzle_->is_finished()) {
        QMessageBox::information(this, tr("Congratulations"),
                                 tr("Game finished!"));
        puzzle_->shuffle();
        update_all_buttons();
    }
}
