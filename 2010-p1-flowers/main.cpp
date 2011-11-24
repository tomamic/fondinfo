/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
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

    while (!puzzle.isWon() && !puzzle.isLost()) {
        int moveY, moveX;
        cin >> moveY >> moveX;
        if (moveY < 0 || moveX < 0) {
            puzzle.flag(abs(moveY) - 1, abs(moveX) - 1);
        } else {
            puzzle.uncover(moveY - 1, moveX - 1);
        }
        puzzle.write(cout);
    }

    cout << (puzzle.isWon() ? "Game won!" : "Game lost!") << endl;
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

    //return runConsole(argc, argv);
    return runGui(argc, argv);
}
