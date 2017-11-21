#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "akari.h"
#include "gamegui.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game();
    void load_game();
    void suggest();
private:
    Akari* game_ = nullptr;
    GameGui* gui_ = nullptr;
};

#endif // MAINWINDOW_H
