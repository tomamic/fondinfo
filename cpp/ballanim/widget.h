#ifndef WIDGET_H
#define WIDGET_H

#include <QtWidgets>
#include <vector>
#include "ball.h"

class Widget : public QWidget
{
    Q_OBJECT
private:
    std::vector<Ball*> balls = {new Ball(40, 80), new Ball(80, 40)};
    QPixmap image{"../../bounce/ball.png"};
public:
    void timerEvent(QTimerEvent *event);
    void paintEvent(QPaintEvent *event);
    void keyPressEvent(QKeyEvent *event);
    Widget();
    ~Widget();
};

#endif // WIDGET_H
