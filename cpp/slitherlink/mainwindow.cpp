#include "mainwindow.h"
#include "gamegui.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QFileDialog>

using namespace std;

MainWindow::MainWindow()
{
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game3 = menu->addAction(tr("5x4"));
    auto game4 = menu->addAction(tr("5x5"));

    connect(game3, &QAction::triggered, [=]{ new_game("../slitherlink/game_5x4.txt"); });
    connect(game4, &QAction::triggered, [=]{ new_game("../slitherlink/game_5x5.txt"); });

    setWindowTitle(tr("Slitherlink Puzzle"));

    new_game("../slitherlink/game_5x5.txt");
}

void MainWindow::new_game(string filename)
{
//    filename = QFileDialog::getOpenFileName(this, tr("Open Game"),
//        "../slitherlink", tr("Game Files (*.txt)")).toStdString();
    if (puzzle_ != nullptr) delete puzzle_;
    if (centralWidget() != nullptr) delete centralWidget();

    puzzle_ = new Slitherlink{filename};
    setCentralWidget(new GameGui(puzzle_));
    adjustSize();
}

