/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef BOARDGAMEGUI_H
#define BOARDGAMEGUI_H

#include "canvas.hpp"
#include <chrono>
#include <functional>

using namespace std::chrono_literals;

namespace g2d {

auto W = 40, H = 40;
auto LONG_PRESS = 0.5s;

class BoardGameGui {
    BoardGame* g_;
    std::chrono::time_point<std::chrono::high_resolution_clock> downtime_, zero_;
    int cols_, rows_;

public:
    BoardGameGui(BoardGame* game) {
        g_ = game; cols_ = g_->cols(); rows_ = g_->rows();
        init_canvas({W*cols_, H*rows_});
        update_buttons();

        main_loop([&]{ tick(); });
    }

    void tick() {
        if (current_keys().count("LeftButton") && downtime_ == zero_) {
            downtime_ = std::chrono::high_resolution_clock::now();
        } else if (! current_keys().count("LeftButton") && downtime_ != zero_) {
            auto pos = mouse_pos();
            auto now = std::chrono::high_resolution_clock::now();
            if (now - downtime_ > LONG_PRESS) {
                g_->flag_at(pos.x/W, pos.y/H);
            } else {
                g_->play_at(pos.x/W, pos.y/H);
            }
            update_buttons();
            downtime_ = zero_;
        }
    }

    void update_buttons() {
        clear_canvas();
        set_color({0, 0, 0});
        for (auto y = 0; y < rows_; ++y) {
            draw_line({0, y * H}, {cols_ * W, y * H});
        }
        for (auto x = 0; x < cols_; ++x) {
            draw_line({x * W, 0}, {x * W, rows_ * H});
        }
        for (auto y = 0; y < rows_; ++y) {
            for (auto x = 0; x < cols_; ++x) {
                auto value = g_->value_at(x, y);
                auto center = Point{x * W + W/2, y * H + H/2};
                draw_text_centered(value, center, H/2);
            }
        }
        if (g_->finished()) {
            alert(g_->message());
            close_canvas();
        }
    }
};

void gui_play(BoardGame* game) {
    auto ui = BoardGameGui{game};
}

}

#endif
