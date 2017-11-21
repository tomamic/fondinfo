#include "mainwindow.h"
#include "boardgamegui.h"
#include "knightdom.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QInputDialog>

MainWindow::MainWindow()
{
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game = menu->addAction(tr("New game"));
    connect(game, &QAction::triggered, this, &MainWindow::new_game);

    setWindowTitle(tr("Knights Domination"));

    new_game();
}

void MainWindow::new_game()
{
    if (game_ != nullptr) delete game_;
    if (centralWidget() != nullptr) delete centralWidget();

    auto side = QInputDialog::getInt(this, "Side", "Side", 4, 1, 16);
    game_ = new KnightDom{side};
    setCentralWidget(new BoardGameGui{game_});

    // fix appearance
    adjustSize();
    setFixedSize(sizeHint());
}

