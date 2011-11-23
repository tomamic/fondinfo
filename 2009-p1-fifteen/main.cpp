#include "fifteenpuzzle.h"
#include "fifteengui.h"

#include <QtGui/QApplication>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;

void runConsole(QApplication& a)
{
    char symbol;
    FifteenPuzzle* puzzle = new FifteenPuzzle(2, 3);
    puzzle->write(cout);

    while (!puzzle->isSolved()) {
        cin >> symbol;
        puzzle->move(toupper(symbol));
        puzzle->write(cout);
    }
    cout << "Puzzle solved!" << endl;
    delete puzzle;
    return 0;
}

void runGui(QApplication& a)
{
    FifteenPuzzle* puzzle = new FifteenPuzzle(2, 3);
    FifteenGui* gui = new FifteenGui(puzzle);
    return a.exec();
}

int main(int argc, char *argv[])
{    
    QApplication a(argc, argv);
    srand(time(NULL));

    // return runConsole(a);
    return runGui(a);
}
