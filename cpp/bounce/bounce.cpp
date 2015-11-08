#include "bounce.h"


Ghost::Ghost(Arena* arena, int x, int y) {
    x_ = x; y_ = y;
    arena_ = arena;
    arena->add(this);
}

void Ghost::move() {
    auto dx = (rand() % 3 - 1) * SPEED;
    auto dy = (rand() % 3 - 1) * SPEED;
    auto as = arena_->rect();
    x_ = (x_ + dx + as.w) % as.w;
    y_ = (y_ + dy + as.h) % as.h;
    if (rand() % 100 == 0) {
        visible_ = !visible_;
    }
}

void Ghost::collide(Actor* other) { }

Rect Ghost::rect() { return {x_, y_, W, H}; }

Rect Ghost::symbol() {
    if (visible_) return {20, 0, W, H};
    return {20, 20, W, H};
}


Ball::Ball(Arena* arena, int x, int y) {
    x_ = x; y_ = y;
    dx_ = SPEED; dy_ = SPEED;
    arena_ = arena;
    arena->add(this);
}

void Ball::move() {
    auto as = arena_->rect();
    if (!(0 <= x_ + dx_ &&  x_ + dx_<= as.w - W)) {
        dx_ = -dx_;
    }
    if (!(0 <= y_ + dy_ &&  y_ + dy_<= as.h - H)) {
        dy_ = -dy_;
    }
    x_ += dx_;
    y_ += dy_;
}

void Ball::collide(Actor* other) {
    auto ghost = dynamic_cast<Ghost*>(other);
    if (ghost == nullptr) {
        auto op = other->rect();
        if (op.x < x_) {
            dx_ = SPEED;
        } else {
            dx_ = -SPEED;
        }
        if (op.y < y_) {
            dy_ = SPEED;
        } else {
            dy_ = -SPEED;
        }
    }
}

Rect Ball::rect() { return {x_, y_, W, H}; }

Rect Ball::symbol() { return {0, 0, W, H}; }


Turtle::Turtle(Arena* arena, int x, int y) {
    x_ = x; y_ = y;
    dx_ = 0; dy_ = 0;
    arena_ = arena;
    arena->add(this);
}

void Turtle::move() {
    auto as = arena_->rect();
    y_ += dy_;
    if (y_ < 0) {
        y_ = 0;
    } else if (y_ > as.h - H) {
        y_ = as.h - H;
    }
    x_ += dx_;
    if (x_ < 0) {
        x_ = 0;
    } else if (x_ > as.w - W) {
        x_ = as.w - W;
    }
}

void Turtle::collide(Actor* other) { }

Rect Turtle::rect() { return {x_, y_, W, H}; }

Rect Turtle::symbol() { return {0, 20, W, H}; }

void Turtle::go_left() { dx_ = -SPEED; dy_ = 0; }

void Turtle::go_right() { dx_ = SPEED; dy_ = 0; }

void Turtle::go_up() { dx_ = 0; dy_ = -SPEED; }

void Turtle::go_down() { dx_ = 0; dy_ = SPEED; }

void Turtle::stay() { dx_ = 0; dy_ = 0; }
