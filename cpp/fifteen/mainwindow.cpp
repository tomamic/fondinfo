#include "mainwindow.h"
#include "gamegui.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>

MainWindow::MainWindow(Fifteen* puzzle)
{
    puzzle_ = puzzle;
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game3 = menu->addAction(tr("3x3"));
    auto game4 = menu->addAction(tr("4x4"));

    connect(game3, &QAction::triggered, [=]{ new_game(3, 3); });
    connect(game4, &QAction::triggered, [=]{ new_game(4, 4); });

    setWindowTitle(tr("Fifteen Puzzle"));

    new_game();
}

void MainWindow::new_game(int cols, int rows)
{
    if (cols > 0 && rows > 0) puzzle_->init(cols, rows);
    if (centralWidget() != nullptr) {
        delete centralWidget();
    }
    setCentralWidget(new GameGui(puzzle_));
    adjustSize();
}

