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

#include <QtGui/QApplication>
#include <QtGui/QInputDialog>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;

int runConsole(int argc, char *argv[])
{
    char symbol;
    FifteenPuzzle puzzle(2, 3);
    puzzle.write(cout);

    while (!puzzle.isSolved()) {
        cin >> symbol;
        puzzle.move(toupper(symbol));
        puzzle.write(cout);
    }
    cout << "Puzzle solved!" << endl;
    return 0;
}

int runGui(int argc, char *argv[])
{
    QApplication a(argc, argv);

    int rows = QInputDialog::getInt(NULL, "Rows?", "Rows?", 4, 2, 20);
    int columns = QInputDialog::getInt(NULL, "Cols?", "Cols?", 4, 2, 20);
    FifteenPuzzle puzzle(rows, columns);
    FifteenGui gui(&puzzle);

    return a.exec();
}

int main(int argc, char *argv[])
{    
    srand(time(NULL));

//    return runConsole(argc, argv);
    return runGui(argc, argv);
}
