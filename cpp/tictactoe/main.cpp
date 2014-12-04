#include <iostream>

#include <QApplication>

#include "tictactoe.h"
#include "gamegui.h"

using namespace std;

int run_console() {
    auto game = TicTacToe{3};
    cout << game.str() << endl;

    int x, y;
    cout << "x, y? ";
    cin >> x >> y;
    while (0 <= x && x < game.side()
           && 0 <= y && y < game.side()) {
        game.play_at(x, y);
        cout << game.str() << endl;
        auto winner = game.winner();
        if (winner != TicTacToe::NONE) {
            cout << "Game finished. " << winner << " has won!" << endl;
            game.reset(game.side());
            cout << game.str() << endl;
        }
        cout << "x, y? ";
        cin >> x >> y;
    }
    return 0;
}

int main(int argc, char* argv[])
{
    // return run_console();

    QApplication a(argc, argv);
    GameGui w{new TicTacToe{3}};
    w.show();
    return a.exec();
}

