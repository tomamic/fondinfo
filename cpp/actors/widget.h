#ifndef WIDGET_H
#define WIDGET_H

#include <QtWidgets>
#include <vector>
#include "actor.h"
#include "car.h"

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget();
    ~Widget();

protected:
    void timerEvent(QTimerEvent *);
    void paintEvent(QPaintEvent *);

private:
    std::vector<Actor*> actors_;
};

#endif // WIDGET_H
