/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QtWidgets>
#include <cstdlib>
#include <ctime>
#include "fifteen.h"
#include "slitherlink.h"
#include "gamegui.h"
#include "mainwindow.h"

using namespace std;

int main_console() {
    Fifteen puzzle{4, 4};
    puzzle.write(cout);

    while (!puzzle.finished()) {
        auto val = 0;
        cout << endl << "Move? ";
        cin >> val;

        puzzle.move_val(val);

        cout << endl;
        puzzle.write(cout);
    }
    cout << "Puzzle solved!" << endl;
    return 0;
}

int main(int argc, char* argv[])
{
    srand(time(nullptr));
    //return main_console();

    QApplication a{argc, argv};
    //Slitherlink puzzle;
    //GameGui gui{&puzzle}; gui.show();
    MainWindow window; window.show();

    return a.exec();
}
