/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include "g2d/basic.hpp"

const int ARENA_W = 480, ARENA_H = 360, BALL_W = 20, BALL_H = 20;

class Ball {
    int x_, y_;
    int dx_ = 5, dy_ = 5;
public:
    Ball(int x, int y) { x_ = x; y_ = y; }
    Ball(g2d::Point pos) { x_ = pos.x; y_ = pos.y; }

    void move() {
        if (x_+dx_ < 0 || x_+dx_+BALL_W > ARENA_W) {
            dx_ = -dx_;
        }
        if (y_+dy_ < 0 || y_+dy_+BALL_H > ARENA_H) {
            dy_ = -dy_;
        }
        x_ += dx_; y_ += dy_;
    }

    g2d::Rect position() { return {x_, y_, BALL_W, BALL_H}; }
};

int main() {
    auto ball1 = Ball{{40, 80}};
    auto ball2 = new Ball{{80, 40}};

    for (auto i = 0; i < 25; ++i) {
        ball1.move();
        ball2->move();

        std::cout << ball1.position() << std::endl;
        std::cout << ball2->position() << std::endl << std::endl;
    }

    delete ball2;
}
