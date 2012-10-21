#include "ball.h"

Ball::Ball(int x, int y, int dx, int dy)
{
    this->x = x;
    this->y = y;
    this->dx = dx;
    this->dy = dy;
}

void Ball::move() {
    if (x + dx < 0 || x + dx >= WIDTH) {
        dx = -dx;
    }
    if (y + dy < 0 || y + dy >= HEIGHT) {
        dy = -dy;
    }
    x += dx;
    y += dy;
}

int Ball::getX() {
    return x;
}

int Ball::getY() {
    return y;
}
