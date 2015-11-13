#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "fifteen.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(Fifteen* game);
    void new_game(int cols=0, int rows=0);

private:
    Fifteen* puzzle_;
};

#endif // MAINWINDOW_H
