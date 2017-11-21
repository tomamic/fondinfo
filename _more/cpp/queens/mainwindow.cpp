#include "mainwindow.h"
#include "gamegui.h"
#include "queens.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QInputDialog>

MainWindow::MainWindow()
{
    setWindowTitle(tr("N Queens"));
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game_act = menu->addAction(tr("New game"));
    connect(game_act, &QAction::triggered,
            this, &MainWindow::new_game);
    new_game();
}

void MainWindow::new_game()
{
    if (centralWidget() != nullptr) delete centralWidget();
    if (game_ != nullptr) delete game_;

    auto side = QInputDialog::getInt(this, "Side", "Side", 1, 1, 20);
    game_ = new Queens{side};
    setCentralWidget(new GameGui{game_});

    // fix appearance
    adjustSize();
    setFixedSize(sizeHint());
}
