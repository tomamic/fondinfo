/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "bounce.hpp"
#include "g2d/canvas.hpp"
#include <iostream>

auto arena = new Arena{{480, 360}};

void tick() {
    arena->tick(g2d::current_keys());
    clear_canvas();
    for (auto a : arena->actors()) {
        draw_image_clip("sprites.png", a->pos(), a->sprite(), a->size());
    }
}

int main() {
    arena->spawn(new Ball{{40, 80}});
    arena->spawn(new Ball{{80, 40}});
    arena->spawn(new Ghost{{120, 80}});
    arena->spawn(new Turtle{{80, 80}});
    init_canvas(arena->size());
    main_loop(tick);
}

int main_console() {
    for (std::string line; std::getline(std::cin, line);) {
        arena->tick({line});
        for (auto a : arena->actors()) {
            auto pos = a->pos();
            std::cout << pos.x << " " << pos.y << std::endl;
        }
        std::cout << std::endl;
    }
    return 0;
}
