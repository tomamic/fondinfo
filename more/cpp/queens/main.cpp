/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include "mainwindow.h"

using namespace std;

int main(int argc, char* argv[])
{
    QApplication a{argc, argv};

    MainWindow window; window.show();

    return a.exec();
}
