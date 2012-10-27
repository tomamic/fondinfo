/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "flowerspuzzle.h"
#include "flowersgui.h"

#include <QtGui/QApplication>
#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>

using namespace std;

int runConsole(int argc, char *argv[])
{
    FlowersPuzzle puzzle(9, 9, 10);
    puzzle.write(cout);

    int moveY, moveX;
    cin >> moveY >> moveX;
    while (cin.good() && !puzzle.isWon() && !puzzle.isLost()) {
        if (moveY < 0 || moveX < 0) {
            puzzle.flag(abs(moveY) - 1, abs(moveX) - 1);
        } else {
            puzzle.uncover(moveY - 1, moveX - 1);
        }
        puzzle.write(cout);

        if (puzzle.isWon()) {
            cout << "Game won!" << endl;
        } else if (puzzle.isLost()) {
            cout << "Game lost!" << endl;
        } else {
            cin >> moveY >> moveX;
        }
    }

    return 0;
}

int runGui(int argc, char *argv[])
{
    QApplication a(argc, argv);

    FlowersPuzzle puzzle(9, 9, 10);
    FlowersGui gui(&puzzle);

    return a.exec();
}

int main(int argc, char *argv[])
{
    srand(time(NULL));

//    return runGui(argc, argv);
    return runConsole(argc, argv);
}
