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
#include <cstdlib>
#include <ctime>

using namespace std;

int runConsole(int argc, char* argv[])
{
    char symbol;
    FifteenPuzzle puzzle(2, 3);
    puzzle.write(cout);

    cin >> symbol;
    while (cin.good() && !puzzle.isFinished()) {
        puzzle.move(toupper(symbol));
        puzzle.write(cout);

        if (puzzle.isFinished()) {
            cout << "Puzzle solved!" << endl;
        } else {
            cin >> symbol;
        }
    }
    return 0;
}

int runGui(int argc, char* argv[])
{
    QApplication a(argc, argv);
    a.setApplicationName(QObject::tr("Fifteen Puzzle"));
    // a.setStyleSheet("FifteenGui {background: green; }"
    //                 "FifteenGui QPushButton { background: yellow; }");

    int rows = QInputDialog::getInt(NULL, "Rows?", "Rows?", 4, 2, 20);
    int columns = QInputDialog::getInt(NULL, "Cols?", "Cols?", 4, 2, 20);
    FifteenPuzzle puzzle(rows, columns);
    FifteenGui gui(&puzzle);

    return a.exec();
}

int main(int argc, char* argv[])
{    
    srand(time(NULL));

    return runGui(argc, argv);
    // return runConsole(argc, argv);
}
