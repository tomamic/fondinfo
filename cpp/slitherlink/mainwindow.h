#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "fifteen.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game(int cols, int rows);

private:
    Fifteen* puzzle_ = nullptr;
};

#endif // MAINWINDOW_H
