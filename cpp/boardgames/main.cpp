/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteen.hpp"
#include "lightsout.hpp"
#include "boardgame_g2d.hpp"

int main_console() {
    //auto game = new LightsOut{4, 5, 5};
    auto game = new Fifteen{4, 4};
    play_game(game);
    return 0;
}

int main() {
    //return main_console();
    auto g = new Fifteen{3, 3};
    gui_play(g);
}
