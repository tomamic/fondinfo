#include <iostream>

#include "tictactoe.h"

using namespace std;

int main()
{
    auto game = TicTacToe(4);
    cout << game.str() << endl;

    int x, y;
    cout << "x, y? ";
    cin >> x >> y;
    while (x >= 0 && y >= 0) {
        game.play_at(x, y);
        cout << game.str() << endl;
        auto winner = game.winner();
        if (winner != TicTacToe::NONE) {
            cout << "Game finished. " << winner << " has won!" << endl;
            game.clear();
            cout << game.str() << endl;
        }
        cout << "x, y? ";
        cin >> x >> y;
    }
}

