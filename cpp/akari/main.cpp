/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include <iostream>
#include "mainwindow.h"
#include "gamegui.h"
#include "queens.h"
#include "akari.h"

using namespace std;

void run_console() {
    auto game = new Akari; // new Queens{6};
    cout << game->to_string() << endl;

    while (!game->finished()) {
        auto x = 0, y = 0;
        cout << "x? y?" << endl;
        cin >> x >> y;

        game->play_at(x, y);

        cout << game->to_string() << endl;
    }
    cout << "Puzzle solved!" << endl;
    delete game;
}

int main(int argc, char* argv[])
{
    /*
    QApplication a{argc, argv};

    //MainWindow window; window.show();

    auto game = new Queens{6}; // = new Akari;
    GameGui gui(game); gui.show();

    return a.exec();
    */

    run_console();
}
