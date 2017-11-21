/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include "notepad.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Notepad window;

    return a.exec();
}
