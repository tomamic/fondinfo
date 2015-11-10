#include <QtWidgets>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    //auto n = QInputDialog::getInt(nullptr, "N", "N?", 5);

    QPixmap screen{600, 400}; QPainter painter{&screen};

    painter.setBrush(QColor{255, 255, 0});
    painter.drawRect(50, 75, 90, 50);

    painter.setBrush(QColor{0, 0, 255});
    painter.drawEllipse(QPoint{300, 50}, 20, 20);

    QLabel label; label.setPixmap(screen); label.show();

    return a.exec();
}
