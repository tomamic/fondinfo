#include "widget.h"
#include "car.h"
#include "skier.h"

Widget::Widget()
{
    actors_.push_back(new Car{10, 110, 5});
    actors_.push_back(new Car{10, 150, 5});
    actors_.push_back(new Car{10, 190, -5});
    actors_.push_back(new Skier{30, 10, 50});
    actors_.push_back(new Skier{80, 20, 50});

    startTimer(1000 / 30);
}

Widget::~Widget()
{
    while (! actors_.empty()) {
        auto a = actors_.back();
        delete a;
        actors_.pop_back();
    }
}

void Widget::timerEvent(QTimerEvent * evt)
{
    for (auto a : actors_) {
        a->move();
    }
    update();
}

void Widget::paintEvent(QPaintEvent * evt)
{
    QPainter painter{this};
    for (auto a : actors_) {
        auto x = a->get_x();
        auto y = a->get_y();
        painter.drawRect(x, y, 10, 10);
    }
}
