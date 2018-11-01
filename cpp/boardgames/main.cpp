/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>
#include "lightsout.h"
#include "fifteen.h"

using namespace std;

void print_game(BoardGame* game) {
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            cout << setw(3) << game->get_val(x, y);
        }
        cout << endl;
    }
}

void play_game(BoardGame* game) {
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

int main(int argc, char* argv[])
{
    //auto game = new LightsOut{4, 5, 5};
    auto game = new Fifteen{4, 4};
    play_game(game);
    return 0;
}
