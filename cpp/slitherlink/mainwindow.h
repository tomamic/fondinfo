#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "slitherlink.h"
#include <QMainWindow>
#include <string>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game(std::string filename);

    void find_loop();
private:
    Slitherlink* puzzle_ = nullptr;
};

#endif // MAINWINDOW_H
