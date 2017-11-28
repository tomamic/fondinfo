/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef BOARDGAMEGUI_H
#define BOARDGAMEGUI_H

#include "boardgame.h"

#include <QWidget>

class BoardGameGui : public QWidget
{
    Q_OBJECT

public:
    BoardGameGui(BoardGame* game);
    void handle_click();
    void update_all_buttons();

private:
    BoardGame* game;
};

#endif // BOARDGAMEGUI_H
