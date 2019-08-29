/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using std::cout;
using std::endl;

const int ARENA_W = 480, ARENA_H = 360;

class Ball {
    int x_, y_;
    int dx_ = 5, dy_ = 5;

public:
    static const int W = 20, H = 20;

    Ball(int x0, int y0) {
        x_ = x0;
        y_ = y0;
    }

    void move() {
        if (x_ + dx_ < 0 || x_ + dx_ + W > ARENA_W) dx_ = -dx_;
        if (y_ + dy_ < 0 || y_ + dy_ + H > ARENA_H) dy_ = -dy_;
        x_ += dx_; y_ += dy_;
    }

    int pos_x() {
        return x_;
    }

    int pos_y() {
        return y_;
    }
};

int main() {
    Ball ball1{40, 80};
    auto ball2 = new Ball{80, 40};


    for (auto i = 0; i < 25; ++i) {
        ball1.move();
        ball2->move();

        cout << ball1.pos_x() << ", " << ball1.pos_y() << endl;
        cout << ball2->pos_x() << ", " << ball2->pos_y() << endl << endl;
    }

    delete ball2;
}
