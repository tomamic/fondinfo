/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "fifteenpuzzle.h"
#include "fifteengui.h"

#include <QApplication>
#include <QInputDialog>
#include <QLibraryInfo>
#include <QLocale>
#include <QTranslator>
#include <cstdlib>
#include <ctime>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    srand(time(NULL));

    QTranslator qtTranslator;
    qtTranslator.load(
                "qt_" + QLocale::system().name(),
                QLibraryInfo::location(QLibraryInfo::TranslationsPath));
    a.installTranslator(&qtTranslator);

    // run lupdate/lrelease, first!
    QTranslator myappTranslator;
    myappTranslator.load(
                ":translations/fifteen_" + QLocale::system().name());
    a.installTranslator(&myappTranslator);

    int rows = QInputDialog::getInt(NULL, "Rows?", "Rows?", 4, 2, 20);
    int columns = QInputDialog::getInt(NULL, "Cols?", "Cols?", 4, 2, 20);
    FifteenModel model(rows, columns);
    FifteenGui gui(&model);
    return a.exec();
}
