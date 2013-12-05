#include "tentsgui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    TentsPuzzle puzzle;
    TentsGui w{&puzzle};
    w.show();
    
    return a.exec();
}
