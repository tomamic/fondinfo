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
    BoardGame* game;
public:
    BoardGameGui(BoardGame* game);
    void update_buttons();
};

#endif // BOARDGAMEGUI_H
