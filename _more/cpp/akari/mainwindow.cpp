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

    auto suggest_act = menu->addAction(tr("Suggest"));
    connect(suggest_act, &QAction::triggered,
            this, &MainWindow::suggest);

    new_game();
}

void MainWindow::new_game()
{
    if (centralWidget() != nullptr) delete centralWidget();
    if (game_ != nullptr) delete game_;
    game_ = new Akari;
    gui_ = new GameGui{game_};
    setCentralWidget(gui_);
    adjustSize();
}

void MainWindow::load_game()
{
    auto fn = QFileDialog::getOpenFileName(this);
    if (fn != "") {
        if (centralWidget() != nullptr) delete centralWidget();
        if (game_ != nullptr) delete game_;

        game_ = new Akari{fn.toStdString()};
        gui_ = new GameGui{game_};
        setCentralWidget(gui_);
        adjustSize();
    }
}

void MainWindow::suggest()
{
    // game_->autocomplete();
    gui_->update_all_buttons();
}
