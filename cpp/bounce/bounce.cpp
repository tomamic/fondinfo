#include "bounce.h"


Ghost::Ghost(Arena* arena, int x, int y) {
    x_ = x; y_ = y;
    arena_ = arena;
    arena->add(this);
}

void Ghost::move() {
    auto dx = (rand() % 3 - 1) * SPEED;
    auto dy = (rand() % 3 - 1) * SPEED;
    auto as = arena_->size();
    x_ = (x_ + dx + as[0]) % as[0];
    y_ = (y_ + dy + as[1]) % as[1];
    if (rand() % 100 == 0) {
        visible_ = !visible_;
    }
}

void Ghost::collide(Actor* other) { }

vector<int> Ghost::position() { return {x_, y_, W, H}; }

vector<int> Ghost::symbol() {
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
    auto as = arena_->size();
    if (!(0 <= x_ + dx_ &&  x_ + dx_<= as[0] - W)) {
        dx_ = -dx_;
    }
    if (!(0 <= y_ + dy_ &&  y_ + dy_<= as[1] - H)) {
        dy_ = -dy_;
    }
    x_ += dx_;
    y_ += dy_;
}

void Ball::collide(Actor* other) {
    auto ghost = dynamic_cast<Ghost*>(other);
    if (ghost == nullptr) {
        auto op = other->position();
        if (op[0] < x_) {
            dx_ = SPEED;
        } else {
            dx_ = -SPEED;
        }
        if (op[1] < y_) {
            dy_ = SPEED;
        } else {
            dy_ = -SPEED;
        }
    }
}

vector<int> Ball::position() { return {x_, y_, W, H}; }

vector<int> Ball::symbol() { return {0, 0, W, H}; }


Turtle::Turtle(Arena* arena, int x, int y) {
    x_ = x; y_ = y;
    dx_ = 0; dy_ = 0;
    arena_ = arena;
    arena->add(this);
}

void Turtle::move() {
    auto as = arena_->size();
    y_ += dy_;
    if (y_ < 0) {
        y_ = 0;
    } else if (y_ > as[1] - H) {
        y_ = as[1] - H;
    }
    x_ += dx_;
    if (x_ < 0) {
        x_ = 0;
    } else if (x_ > as[0] - W) {
        x_ = as[0] - W;
    }
}

void Turtle::collide(Actor* other) { }

vector<int> Turtle::position() { return {x_, y_, W, H}; }

vector<int> Turtle::symbol() { return {0, 20, W, H}; }

void Turtle::go_left() { dx_ = -SPEED; dy_ = 0; }

void Turtle::go_right() { dx_ = SPEED; dy_ = 0; }

void Turtle::go_up() { dx_ = 0; dy_ = -SPEED; }

void Turtle::go_down() { dx_ = 0; dy_ = SPEED; }

void Turtle::stay() { dx_ = 0; dy_ = 0; }
