#ifndef WIDGET_H
#define WIDGET_H

#include <QtWidgets>

class Widget : public QWidget
{
    Q_OBJECT
private:
    int x = 0;
    QPixmap image{"../anim/ball.png"};
protected:
    void timerEvent(QTimerEvent *event);
    void paintEvent(QPaintEvent *event);
public:
    Widget();
};

#endif // WIDGET_H
