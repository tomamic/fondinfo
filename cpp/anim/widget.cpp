#include "widget.h"

Widget::Widget() {
    startTimer(1000 / 60);  // 60 fps
}

void Widget::timerEvent(QTimerEvent* event) {
    x = (x + 5) % width();
    update();  // async: this widget should be redrawn
}

void Widget::paintEvent(QPaintEvent* event) {
    QPainter painter{this};
    painter.drawPixmap(x, 10, image);
}
