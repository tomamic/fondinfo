/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/canvas.hpp"

auto x = 50, y = 50, dx = 5, dy = 0;
auto image = g2d::load_image("ball.png");

void tick() {
    if (g2d::key_pressed("LeftButton")) {
        dx = -dx;
    }
    g2d::clear_canvas();
    g2d::draw_image(image, {x, y});
    x += dx;
}

int main() {
    g2d::main_loop(tick);
}
