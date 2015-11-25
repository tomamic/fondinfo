/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef GAMEGUI_H
#define GAMEGUI_H

#include "game.h"

#include <QWidget>

class GameGui : public QWidget
{
    Q_OBJECT

public:
    GameGui(Game* game);
    void handle_click();
    void update_button(int x, int y);
    void update_all_buttons();

private:
    Game* game_;
    int cols_;
    int rows_;
};

#endif // GAMEGUI_H
