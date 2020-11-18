/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "bounce.hpp"
#include "g2d/canvas.hpp"
#include <iostream>

auto arena = new Arena{{480, 360}};
auto b1 = new Ball{arena, {40, 80}};
auto b2 = new Ball{arena, {80, 40}};
auto g = new Ghost{arena, {120, 80}};
auto turtle = new Turtle{arena, {80, 80}};

void tick() {
    turtle->control(g2d::pressed_keys(), g2d::released_keys());

    arena->move_all();
    clear_canvas();
    for (auto a : arena->actors()) {
        draw_image_clip("sprites.png", a->symbol(), a->position());
    }
}

int main() {
    init_canvas(arena->size());
    main_loop(tick);
}

int main_console() {
    for (std::string line; std::getline(std::cin, line);) {
        turtle->control({line}, {"w", "a", "s", "d"});

        arena->move_all();
        for (auto a : arena->actors()) {
            auto pos = a->position();
            std::cout << pos.x << " " << pos.y << std::endl;
        }
        std::cout << std::endl;
    }
    return 0;
}
