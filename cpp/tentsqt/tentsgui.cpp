#include "tentsgui.h"
#include <QGridLayout>
#include <QMessageBox>
#include <QLabel>
#include <iostream>

TentsGui::TentsGui(TentsPuzzle* puzzle) {
    puzzle_ = puzzle;

    auto grid = new QGridLayout;
    setCentralWidget(new QWidget);
    centralWidget()->setLayout(grid);
    for (auto y = 0; y < puzzle_->rows(); ++y) {
        for (auto x = 0; x < puzzle_->cols(); ++x) {
            auto b = new QPushButton;
            buttons_.push_back(b);
            grid->addWidget(b, y, x);
            connect(b, &QPushButton::clicked,
                    [=]{ handle_click(x, y); });
        }
        QLabel* label = new QLabel{std::to_string(y).c_str()};
        grid->addWidget(label, y, puzzle_->cols());
    }
    for (auto x = 0; x < puzzle_->cols(); ++x) {
        QLabel* label = new QLabel{std::to_string(x).c_str()};
        grid->addWidget(label, puzzle_->rows(), x);
    }

    update_all_buttons();
}

TentsGui::~TentsGui() {
}

void TentsGui::update_button(int x, int y) {
    auto val = puzzle_->get(x, y);
    auto b = buttons_[y * puzzle_->cols() + x];
    b->setText(QString{val});
}

void TentsGui::update_all_buttons() {
    for (auto y = 0; y < puzzle_->rows(); y++)
        for (auto x = 0; x < puzzle_->cols(); x++)
            update_button(x, y);
}

void TentsGui::handle_click(int x, int y) {
    puzzle_->place_tent(x, y);
    update_all_buttons();

    if (puzzle_->solved()) {
        QMessageBox::information(this, tr("Congratulations"),
                                 tr("Game finished!"));
        window()->close();
    }
}
