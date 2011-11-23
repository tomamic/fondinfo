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
    GameGui(Game* game, QWidget* parent = NULL);

public slots:
    void updateGame();

private:
    void updateAllLabels();
    void keyPressEvent(QKeyEvent* event);    
    void keyReleaseEvent(QKeyEvent* event);

    Game* game;

    std::vector <QLabel*> labels;
    QTimer* timer;
    static const int PLAYER_1 = 0;
    static const int PLAYER_2 = 1;
};

#endif // GAMEGUI_H
