#include "widget.h"
#include <QtWidgets>

void circles(QPainter& painter, int x, int y, int r, int level)
{
    if (level == 0) return;
    if (level % 2 == 0) {
        painter.setBrush(QColor{255, 255, 0});
    } else {
        painter.setBrush(QColor{0, 255, 0});
    }

    painter.drawEllipse( QPoint{x, y}, r, r);

    circles(painter, x, y - r / 2, r / 2, level - 1);
    circles(painter, x, y + r / 2, r / 2, level - 1);
}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QPixmap screen{600, 600};
    QPainter painter{&screen};

    circles(painter, 300, 300, 300, 10);

    QLabel label;
    label.setPixmap(screen);
    label.setFixedSize(screen.size());
    label.show();

    return a.exec();
}
