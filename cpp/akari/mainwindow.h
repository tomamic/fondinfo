#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "akari.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game();

    void load_game();
private:
    Akari* game_ = nullptr;
};

#endif // MAINWINDOW_H
