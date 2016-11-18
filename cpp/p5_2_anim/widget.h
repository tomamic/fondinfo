#ifndef WIDGET_H
#define WIDGET_H

#include <QtWidgets>

class Widget : public QWidget
{
    Q_OBJECT
private:
    int x = 0;
    int dx = 5;
    QPixmap image{"../../bounce/ball.png"};
public:
    void timerEvent(QTimerEvent *event);
    void paintEvent(QPaintEvent *event);
    void keyPressEvent(QKeyEvent *event);
    Widget();
};

#endif // WIDGET_H
