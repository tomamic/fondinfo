/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QtWidgets>
#include <cstdlib>
#include <ctime>
#include "fifteen.h"
#include "gamegui.h"
#include "mainwindow.h"

using namespace std;

int main_console() {
    Fifteen puzzle{4, 4};
    cout << puzzle.str();
    auto val = 0;
    while (cin >> val) {
        puzzle.move_val(val);
        cout << puzzle.str() << endl;
        if (puzzle.finished()) {
            cout << "Puzzle solved!" << endl;
            puzzle.new_game();
            cout << puzzle.str();
        }
    }
    return 0;
}

int main(int argc, char* argv[])
{
    srand(time(nullptr));
    //return main_console();

    QApplication a{argc, argv};
    Fifteen puzzle{4, 4};
    //MainWindow window{&puzzle}; window.show();
    GameGui gui{&puzzle}; gui.show();

    return a.exec();
}
