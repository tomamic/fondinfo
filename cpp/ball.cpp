/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
using namespace std;

const int ARENA_W = 480, ARENA_H = 360;

class Ball {
    int x_, y_;  // private stuff
    int w_ = 20, h_ = 20;
    int dx_ = 5, dy_ = 5;
public:
    Ball(int x, int y) {  // constructor
        x_ = x; y_ = y;
    }
    void move() {
        if (x_+dx_ < 0 || x_+dx_+w_ > ARENA_W) {
            dx_ = -dx_;
        }
        if (y_+dy_ < 0 || y_+dy_+h_ > ARENA_H) {
            dy_ = -dy_;
        }
        x_ += dx_; y_ += dy_;
    }
    int pos_x() { return x_; }
    int pos_y() { return y_; }
};

int main() {
    auto b1 = Ball{140, 180};
    auto b2 = Ball{180, 140};

    for (auto i = 0; i < 25; ++i) {
        b1.move();
        b2.move();
        cout << b1.pos_x() << " " << b1.pos_y() << endl;
        cout << b2.pos_x() << " " << b2.pos_y() << endl << endl;
    }
}
