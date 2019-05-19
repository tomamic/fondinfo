#include "g2d/canvas.hpp"

void keydown(string key) {
    auto pos = mouse_position();
    if (pos.x < 25 && pos.y < 25 && confirm("Exit?")) {
        close_canvas();
    } else {
        auto radius = 25; //std::stoi(prompt("Radius?"));
        set_color({randint(0, 255), randint(0, 255), randint(0, 255)});
        fill_circle({pos.x, pos.y}, radius);
    }
}

int main() {
    init_canvas({640, 480});
    handle_events(nullptr, keydown, nullptr);
    main_loop();
}
