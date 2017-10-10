#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "boardgame.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game(int cols, int rows);

private:
    BoardGame* game_ = nullptr;
};

#endif // MAINWINDOW_H
