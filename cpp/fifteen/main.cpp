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

void run_gui(int argc, char* argv[]) {
    QApplication a{argc, argv};
    // apply style, from resources
    QFile file{":stylesheet.qss"};
    if (file.open(QFile::ReadOnly))
        a.setStyleSheet(file.readAll());

    auto cols = QInputDialog::getInt(NULL, "Cols?", "Cols?", 4, 2, 20);
    auto rows = QInputDialog::getInt(NULL, "Rows?", "Rows?", 4, 2, 20);
    FifteenPuzzle puzzle{cols, rows};
    FifteenGui gui{&puzzle};

    auto exit_val = a.exec();
    exit(exit_val);
}

int main(int argc, char* argv[])
{
    srand(time(NULL));
    run_gui(argc, argv);

    FifteenPuzzle puzzle{3, 2};
    cout << puzzle.str();
    auto val = 0;
    while (cin >> val) {
        puzzle.move(val);
        cout << puzzle.str() << endl;
        if (puzzle.is_finished()) {
            cout << "Puzzle solved!" << endl;
            break;
        }
    }
}
