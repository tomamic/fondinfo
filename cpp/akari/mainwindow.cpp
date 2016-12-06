#include "mainwindow.h"
#include "gamegui.h"
#include "akari.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QFileDialog>
#include <QLayout>

MainWindow::MainWindow()
{
    setWindowTitle(tr("Akari"));
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game_act = menu->addAction(tr("New"));
    connect(game_act, &QAction::triggered,
            this, &MainWindow::new_game);

    auto load_act = menu->addAction(tr("Load"));
    connect(load_act, &QAction::triggered,
            this, &MainWindow::load_game);

    new_game();
}

void MainWindow::new_game()
{
    if (centralWidget() != nullptr) delete centralWidget();
    if (game_ != nullptr) delete game_;
    game_ = new Akari;
    setCentralWidget(new GameGui{game_});
    adjustSize();
}

void MainWindow::load_game()
{
    auto fn = QFileDialog::getOpenFileName(this);
    if (fn != "") {
        if (centralWidget() != nullptr) delete centralWidget();
        if (game_ != nullptr) delete game_;

        game_ = new Akari{fn.toStdString()};
        setCentralWidget(new GameGui{game_});
        adjustSize();
    }
}
