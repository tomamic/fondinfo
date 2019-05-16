#ifndef BOUNCE_HPP
#define BOUNCE_HPP

#include "../g2d/actor.hpp"
#include <vector>

using std::vector;

class Ghost : public Actor {
private:
    Arena* arena_;
    int x_, y_;
    bool visible_ = true;
    static const int W = 20, H = 20, SPEED = 5;
public:
    Ghost(Arena* arena, Point position) {
        x_ = position.x; y_ = position.y;
        arena_ = arena;
        arena->add(this);
    }
    void move() {
        auto dx = (rand() % 3 - 1) * SPEED;
        auto dy = (rand() % 3 - 1) * SPEED;
        auto as = arena_->size();
        x_ = (x_ + dx + as.w) % as.w;
        y_ = (y_ + dy + as.h) % as.h;
        if (rand() % 100 == 0) {
            visible_ = !visible_;
        }
    }
    void collide(Actor* other) { }
    Rect position() { return {x_, y_, W, H}; }
    Rect symbol() {
        if (visible_) return {20, 0, W, H};
        return {20, 20, W, H};
    }
};


class Ball : public Actor {
private:
    Arena* arena_;
    int x_, y_, dx_, dy_;
    static const int W = 20, H = 20, SPEED = 5;
public:
    Ball(Arena* arena, Point position) {
        x_ = position.x; y_ = position.y;
        dx_ = SPEED; dy_ = SPEED;
        arena_ = arena;
        arena->add(this);
    }
    void move() {
        auto as = arena_->size();
        if (!(0 <= x_ + dx_ &&  x_ + dx_<= as.w - W)) {
            dx_ = -dx_;
        }
        if (!(0 <= y_ + dy_ &&  y_ + dy_<= as.h - H)) {
            dy_ = -dy_;
        }
        x_ += dx_;
        y_ += dy_;
    }
    void collide(Actor* other) {
        auto ghost = dynamic_cast<Ghost*>(other);
        if (ghost == nullptr) {
            auto op = other->position();
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
    Rect position() { return {x_, y_, W, H}; }
    Rect symbol() { return {0, 0, W, H}; }
};


class Turtle : public Actor {
private:
    Arena* arena_;
    int x_, y_, dx_, dy_;
    static const int W = 20, H = 20, SPEED = 2;
public:
    Turtle(Arena* arena, Point position) {
        x_ = position.x; y_ = position.y;
        dx_ = 0; dy_ = 0;
        arena_ = arena;
        arena->add(this);
    }
    void move() {
        auto as = arena_->size();
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
    void collide(Actor* other) { }
    Rect position() { return {x_, y_, W, H}; }
    Rect symbol() { return {0, 20, W, H}; }
    void go_left() { dx_ = -SPEED; dy_ = 0; }
    void go_right() { dx_ = SPEED; dy_ = 0; }
    void go_up() { dx_ = 0; dy_ = -SPEED; }
    void go_down() { dx_ = 0; dy_ = SPEED; }
    void stay() { dx_ = 0; dy_ = 0; }
};

#endif // BOUNCE_HPP
