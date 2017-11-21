/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include <QInputDialog>
#include <QLibraryInfo>
#include <QLocale>
#include <QTranslator>
#include <cstdlib>
#include <ctime>
#include "fifteenpuzzle.h"
#include "fifteengui.h"

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
