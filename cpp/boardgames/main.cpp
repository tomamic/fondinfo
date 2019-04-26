/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "fifteen.hpp"
#include "lightsout.hpp"
#include "boardgame_g2d.hpp"

int main() {
    auto g = new Fifteen{3, 3};  // ... or LightsOut{4, 5, 5};
    gui_play(g);                 // ... or console_play(g);
}
