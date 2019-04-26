#ifndef BOARDGAME_H
#define BOARDGAME_H

#include <iomanip>
#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

class BoardGame
{
public:
    virtual void play_at(int x, int y) = 0;
    virtual void flag_at(int x, int y) = 0;
    virtual int cols() = 0;
    virtual int rows() = 0;
    virtual string value_at(int x, int y) = 0;
    virtual bool finished() = 0;
    virtual string message() = 0;

    virtual ~BoardGame() {}
};


void print_game(BoardGame* game) {
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            cout << std::setw(3) << game->value_at(x, y);
        }
        cout << endl;
    }
}

void console_play(BoardGame* game) {
    print_game(game);

    while (! game->finished()) {
        auto x = 0, y = 0;
        cout << endl << "Move? ";
        cin >> x >> y;

        game->play_at(x, y);
        print_game(game);
    }
    cout << game->message() << endl;
}

#endif // BOARDGAME_H
