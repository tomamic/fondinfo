#include "widget.h"

Widget::Widget() {
    startTimer(1000 / 60);  // 60 fps
}

void Widget::timerEvent(QTimerEvent* event) {
    x = (x + dx + width()) % width();
    update();  // async: this widget should be redrawn
}

void Widget::paintEvent(QPaintEvent* event) {
    QPainter painter{this};
    painter.drawPixmap(x, height() / 2, image);
}

void Widget::keyPressEvent(QKeyEvent *event)
{
    if (event->key() == Qt::Key_Space) {
        dx = -dx;
    }
}
