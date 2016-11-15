#include <iostream>
#include "tictactoe.h"

using namespace std;

void print(TicTacToe* game) {
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            cout << '|' << game->get_val(x, y);
        }
        cout << '|' << endl;
    }
}

int main(int argc, char *argv[])
{
    auto game = new TicTacToe;
    print(game);

    int x, y;
    while (! game->finished()) {
        cin >> x >> y;
        game->play_at(x, y);
        print(game);
    }

    cout << game->message() << endl;

    return 0;
}
