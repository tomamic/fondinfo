#ifndef BOUNCEGUI_H
#define BOUNCEGUI_H

#include <QWidget>
#include <QPixmap>
#include <QPainter>
#include <QTimerEvent>
#include <QPaintEvent>
#include <QKeyEvent>

#include "bounce.h"

class BounceGui : public QWidget
{
    Q_OBJECT
private:
    Arena* arena_;
    Turtle* turtle_;
    QPixmap sprites_{"../bounce/sprites.png"};
public:
    BounceGui();
    void timerEvent(QTimerEvent* event);
    void paintEvent(QPaintEvent* event);
    void keyPressEvent(QKeyEvent* event);
    void keyReleaseEvent(QKeyEvent * event);
};

#endif // BOUNCEGUI_H
