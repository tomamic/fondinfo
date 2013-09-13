#include "notepad.h"
#include "notepadwindow.h"
#include <QApplication>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

//    Notepad n;
//    n.show();

    NotepadWindow w;
    w.show();

    return a.exec();
}
