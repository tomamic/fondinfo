#ifndef GAMEGUI_H
#define GAMEGUI_H

#include <QMainWindow>
#include <QPushButton>

#include "tictactoe.h"

class GameGui : public QMainWindow
{
    Q_OBJECT

public:
    GameGui(TicTacToe* game);

private:
    void handle_click(int x, int y);
    void update_button(int x, int y);
    void update_all_buttons();
    void new_game(int side);
    void create_buttons();

    int cols() { return game_->side(); }
    int rows() { return game_->side(); }

    vector<QPushButton*> buttons_;
    TicTacToe* game_;
};

#endif // GAMEGUI_H
