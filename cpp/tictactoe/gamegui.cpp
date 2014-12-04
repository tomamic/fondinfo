#include "gamegui.h"

#include <QGridLayout>
#include <QMessageBox>
#include <QMenuBar>
#include <QMenu>
#include <QAction>

GameGui::GameGui(TicTacToe* game)
{
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game3 = menu->addAction(tr("3x3"));
    auto game4 = menu->addAction(tr("4x4"));

    connect(game3, &QAction::triggered, [=]{ new_game(3); });
    connect(game4, &QAction::triggered, [=]{ new_game(4); });

    game_ = game;
    create_buttons();
}

void GameGui::create_buttons()
{
    if (centralWidget() != nullptr) {
        delete centralWidget();
    }
    buttons_.clear();
    auto grid = new QGridLayout;
    setCentralWidget(new QWidget);
    centralWidget()->setLayout(grid);
    for (auto y = 0; y < rows(); ++y) {
        for (auto x = 0; x < cols(); ++x) {
            auto b = new QPushButton;
            buttons_.push_back(b);
            grid->addWidget(b, y, x);
            connect(b, &QPushButton::clicked,
                    [=]{ handle_click(x, y); });
        }
    }
    update_all_buttons();
    adjustSize();
}

void GameGui::handle_click(int x, int y)
{
    game_->play_at(x, y);
    update_button(x, y);
    auto winner = game_->winner();
    if (winner != TicTacToe::NONE) {
        QMessageBox::information(this, tr("Game finished!"),
                                 tr("Winner: ") + winner);
        game_->reset(game_->side());
        update_all_buttons();
    }
}

void GameGui::update_button(int x, int y)
{
    auto val = game_->get(x, y);
    auto b = buttons_[y * cols() + x];
    b->setText(QString{val});

    if (val == TicTacToe::NONE) {
        b->setStyleSheet("background: black; color: white");
    } else {
        b->setStyleSheet("background: white; color: black");
    }
}

void GameGui::update_all_buttons()
{
    for (auto y = 0; y < rows(); y++)
        for (auto x = 0; x < cols(); x++)
            update_button(x, y);
}

void GameGui::new_game(int side)
{
    delete game_;
    game_ = new TicTacToe(side);
    create_buttons();
}

