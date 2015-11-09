#include <QtWidgets>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QPixmap screen{600, 400}; QPainter painter{&screen};

    painter.setBrush(QColor{255, 255, 0});
    painter.drawRect(50, 75, 90, 50);

    painter.setBrush(QColor{0, 0, 255});
    painter.drawEllipse(290, 40, 40, 40); // enclosing rect

    QLabel label; label.setPixmap(screen); label.show();

    return a.exec();
}
