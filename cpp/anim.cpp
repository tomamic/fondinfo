#include "g2d/canvas.hpp"

auto x = 50, y = 50, dx = 5, dy = 0;
auto ARENA_W = 480, ARENA_H = 360;
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
    g2d::init_canvas({ARENA_W, ARENA_H});
    g2d::main_loop(tick);
}
