#include "widget.h"

Widget::Widget()
{
    startTimer(1000 / 60);  // 60 fps
    setFixedSize(Ball::ARENA_W, Ball::ARENA_H);
}

Widget::~Widget()
{
    for (auto b : balls) {
        delete b;
    }
}

void Widget::timerEvent(QTimerEvent* event)
{
    for (auto b : balls) {
        b->move();
    }
    update();  // async: this widget should be redrawn
}

void Widget::paintEvent(QPaintEvent* event)
{
    QPainter painter{this};
    for (auto b : balls) {
        painter.drawPixmap(b->get_x(), b->get_y(), image);
    }
}

void Widget::keyPressEvent(QKeyEvent *event)
{
}
