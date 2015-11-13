/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "gamegui.h"

#include <QGridLayout>
#include <QMessageBox>
#include <QPushButton>
#include <QStyle>
#include <QVariant>

GameGui::GameGui(Fifteen* puzzle)
{
    puzzle_ = puzzle;
    cols_ = puzzle->cols();
    rows_ = puzzle->rows();

    auto grid = new QGridLayout; setLayout(grid);
    for (auto y = 0; y < rows_; ++y) {
        for (auto x = 0; x < cols_; ++x) {
            auto b = new QPushButton;
            b->setFixedSize(50, 50);
            grid->addWidget(b, y, x);
            connect(b, &QPushButton::clicked,
                    [=]{ handle_click(x, y); });
        }
    }
    update_all_buttons();
}

void GameGui::update_button(int x, int y) {
    auto val = puzzle_->get(x, y);
    string symbol = "";
    if (val > 0) symbol = to_string(val);

    auto b = layout()->itemAt(y * cols_ + x)->widget();
    dynamic_cast<QPushButton*>(b)->setText(symbol.c_str());
}

void GameGui::update_all_buttons() {
    for (auto y = 0; y < rows_; y++) {
        for (auto x = 0; x < cols_; x++) {
            update_button(x, y);
        }
    }
}

void GameGui::handle_click(int x, int y)
{
    puzzle_->move_pos(x, y);
    update_all_buttons();  // ...

    if (puzzle_->is_finished()) {
        QMessageBox::information(nullptr, tr("Congratulations"),
                                 tr("Game finished!"));
        puzzle_->new_game();
        update_all_buttons();
    }
}
