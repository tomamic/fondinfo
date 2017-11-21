/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef GAMEGUI_H
#define GAMEGUI_H

#include "game.h"

#include <QtGui/QWidget>
#include <QtGui/QLabel>
#include <QtGui/QKeyEvent>
#include <QtCore/QTimer>
#include <vector>

class GameGui : public QWidget
{
    Q_OBJECT

public:
    GameGui(Game* game);

public slots:
    void updateGame();

private:
    void updateAllLabels();
    void keyPressEvent(QKeyEvent* event);    
    void keyReleaseEvent(QKeyEvent* event);

    Game* game;

    std::vector <QLabel*> labels;
    QTimer* timer;
};

#endif // GAMEGUI_H
