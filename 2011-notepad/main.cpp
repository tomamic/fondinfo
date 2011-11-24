/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2011
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <QtGui/QApplication>
#include "notepad.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Notepad window;

    return a.exec();
}
