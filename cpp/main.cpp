#include "g2d/canvas.hpp"

void keydown(string key) {
    auto pos = mouse_position();
    set_color({randint(0, 255), randint(0, 255), randint(0, 255)});
    fill_circle({pos.x, pos.y}, 25);
    if (pos.x <= 10 && pos.y <= 10) {
        close_canvas();
    }
}

int main() {
    init_canvas({640, 480});
    while (confirm("circle?")) {
        auto r = 25; //stoi(prompt("r? "));
        fill_circle({randint(0, 255), randint(0, 255)}, r);
        update_canvas();
    }
    handle_events(nullptr, keydown, nullptr);
    main_loop();
}
