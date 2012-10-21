#include "ball.h"

Ball::Ball(int x, int y, int dx, int dy,
           int width, int height) {
    this->x = x;
    this->y = y;
    this->dx = dx;
    this->dy = dy;
    this->width = width;
    this->height = height;
}

void Ball::move() {
    if (x + dx < 0 || x + dx >= width) {
        dx = -dx;
    }
    if (y + dy < 0 || y + dy >= height) {
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
