#include "bouncegui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    BounceGui w;
    w.show();

    return a.exec();
}
