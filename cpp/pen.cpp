#include "g2d/canvas.hpp"
#include <cmath>
#include <vector>

std::vector<double> move_pen(double x, double y, double length, double angle) {
    auto x1 = x + cos(angle) * length;
    auto y1 = y + sin(angle) * length;
    g2d::draw_line({int(x), int(y)}, {int(x1), int(y1)});
    return {x1, y1};
}

int main() {
    g2d::init_canvas({600, 600});

    auto n = 3;  // triangle
    auto x = 200.0, y = 200.0;
    auto side = 200.0, angle = 0.0;  // →

    for (auto i = 0; i < n; ++i) {
        auto pos = move_pen(x, y, side, angle);
        x = pos[0], y = pos[1];
        angle += 2 * M_PI / n;  // ↻ 120°
    }
    g2d::main_loop();
}
