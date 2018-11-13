#include "ball.h"

using namespace std;

Ball::Ball(int x0, int y0) {
    x_ = x0;
    y_ = y0;
}

void Ball::move() {
    if (x_ + dx_ < 0 || x_ + dx_ + W > ARENA_W) dx_ = -dx_;
    if (y_ + dy_ < 0 || y_ + dy_ + H > ARENA_H) dy_ = -dy_;
    x_ += dx_; y_ += dy_;
}

int Ball::get_x() {
    return x_;
}

int Ball::get_y() {
    return y_;
}
