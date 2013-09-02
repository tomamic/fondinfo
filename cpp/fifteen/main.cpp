/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include <QFile>
#include <QInputDialog>
#include <cstdlib>
#include <ctime>
#include "fifteenpuzzle.h"
#include "fifteengui.h"

using namespace std;

int main(int argc, char* argv[])
{
    srand(time(NULL));
    auto retval = 0;
    if (argc > 1 && string(argv[1]) == "-nogui") {
        FifteenPuzzle puzzle{3, 2};
        cout << puzzle.str();
        char symbol;
        while (cin >> symbol) {
            puzzle.move(toupper(symbol));
            cout << puzzle.str();
            if (puzzle.finished()) {
                cout << "Puzzle solved!" << endl;
                break;
            }
        }
    } else {
        QApplication a{argc, argv};

        // apply style, from resources
        QFile file{":stylesheet.qss"};
        if (file.open(QFile::ReadOnly)) {
            a.setStyleSheet(file.readAll());
        }

        int cols = QInputDialog::getInt(NULL, "Cols?", "Cols?", 4, 2, 20);
        int rows = QInputDialog::getInt(NULL, "Rows?", "Rows?", 4, 2, 20);
        FifteenPuzzle puzzle{cols, rows};
        FifteenGui gui{&puzzle};

        retval = a.exec();
    }
    return retval;
}
