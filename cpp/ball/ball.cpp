#include "ball.h"

using namespace std;

Ball::Ball(int x0, int y0) {
    x = x0;
    y = y0;
}

void Ball::move() {
    x += dx; y += dy;
    if (!(0 <= x && x < ARENA_W - W)) dx = -dx;
    if (!(0 <= y && y < ARENA_H - H)) dy = -dy;
}

int Ball::get_x() {
    return x;
}

int Ball::get_y() {
    return y;
}
