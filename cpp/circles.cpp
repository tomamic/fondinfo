/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/canvas.hpp"

void update() {
    if (g2d::key_pressed("LeftButton")) {
        auto pos = g2d::mouse_position();
        if (pos.x < 25 && pos.y < 25 && g2d::confirm("Exit?")) {
            g2d::close_canvas();
        } else {
            auto radius = 25;
            g2d::set_color({g2d::randint(0, 255),
                            g2d::randint(0, 255),
                            g2d::randint(0, 255)});
            g2d::fill_circle({pos.x, pos.y}, radius);
        }
    }
}

int main() {
    g2d::init_canvas({640, 480});
    g2d::main_loop(update);
}
