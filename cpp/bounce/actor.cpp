#include "actor.h"

Arena::Arena(int width, int height) {
    w_ = width;
    h_ = height;
}

void Arena::add(Actor* a) {
    auto pos = find(begin(actors_), end(actors_), a);
    if (pos == actors_.end()) {
        actors_.push_back(a);
    }
}

void Arena::remove(Actor* a) {
    auto pos = find(begin(actors_), end(actors_), a);
    if (pos != actors_.end()) {
        actors_.erase(pos);
    }
}

void Arena::move_all() {
    auto acts = actors();
    reverse(begin(acts), end(acts));
    for (auto a : acts) {
        auto prev = a->rect();
        a->move();
        auto curr = a->rect();
        if (curr.x != prev.x || curr.y != prev.y
                || curr.w != prev.w || curr.h != prev.h) {
            for (auto other : acts) {
                if (other != a && check_collision(a, other)) {
                    a->collide(other);
                    other->collide(a);
                }
            }
        }
    }
}

bool Arena::check_collision(Actor* a1, Actor* a2) {
    auto r1 = a1->rect();
    auto r2 = a2->rect();
    return (r2.y < r1.y + r1.h && r1.y < r2.y + r2.h
        && r2.x < r1.x + r1.w and r1.x < r2.x + r2.w);
}

vector<Actor*> Arena::actors() { return actors_; }

Rect Arena::rect() { return {0, 0, w_, h_}; }

Arena::~Arena() {
    while (!actors_.empty()) {
        delete actors_.back();
        actors_.pop_back();
    }
}
