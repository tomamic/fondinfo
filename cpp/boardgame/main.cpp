/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
//#include "mainwindow.h"
#include <iostream>
#include <iomanip>
#include "knightdom.h"
#include "boardgamegui.h"
#include "mainwindow.h"

using namespace std;

void print_game(BoardGame* game) {
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            cout << setw(3) << game->get_val(x, y);
        }
        cout << endl;
    }
}

int console_play(BoardGame* game) {
    print_game(game);

    while (! game->finished()) {
        auto x = 0, y = 0;
        cout << endl << "Move? ";
        cin >> x >> y;

        game->play_at(x, y);
        print_game(game);
    }
    cout << game->message() << endl;
    return 0;
}

int main(int argc, char* argv[])
{
    auto game = new KnightDom{6};
//    return console_play(game);

    QApplication a{argc, argv};
    BoardGameGui gui{game}; gui.show();

    //MainWindow window; window.show();

    return a.exec();
}
