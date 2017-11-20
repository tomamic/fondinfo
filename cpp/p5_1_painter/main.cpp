#include <QtWidgets>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    auto n = QInputDialog::getInt(nullptr, "N", "N?", 5);

    QPixmap screen{600, 400};
    screen.fill(QColor{255, 255, 255});
    QPainter painter{&screen};

    for (auto i = 0; i < n; ++i) {
        painter.setBrush(QColor{255, 255, 0});
        painter.setPen(QColor{255, 255, 255});
        painter.drawRect(50 + i *10, 75 + i * 15, 90, 50);
    }

    painter.setBrush(QColor{0, 0, 255});
    painter.drawEllipse(QPoint{300, 50}, 20, 20);

    QLabel label;
    label.setPixmap(screen);
    label.show();

    return a.exec();
}
