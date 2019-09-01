/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef ACTOR_HPP
#define ACTOR_HPP

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <ctime>

namespace g2d {

struct Point {
    int x, y;
};
struct Rect {
    int x, y, w, h;
};
struct Color {
    int r, g, b;
};

class Actor {
public:
    virtual void move() = 0;
    virtual void collide(Actor* other) = 0;
    virtual Rect position() = 0;
    virtual Rect symbol() = 0;
    virtual ~Actor() {}
};

class Arena {
private:
    int w_, h_;
    std::vector<Actor*> actors_;
public:
    Arena(Point size) { w_ = size.x; h_ = size.y; }
    void add(Actor* a) {
        auto pos = find(begin(actors_), end(actors_), a);
        if (pos == end(actors_)) {
            actors_.push_back(a);
        }
    }
    void remove(Actor* a) {
        auto pos = find(begin(actors_), end(actors_), a);
        if (pos != end(actors_)) {
            actors_.erase(pos);
        }
    }
    void move_all() {
        auto acts = actors();
        reverse(begin(acts), end(acts));
        for (auto a : acts) {
            a->move();
            for (auto other : acts) {
                if (other != a && check_collision(a, other)) {
                    a->collide(other);
                    other->collide(a);
                }
            }
        }
    }
    bool check_collision(Actor* a1, Actor* a2) {
        auto r1 = a1->position();
        auto r2 = a2->position();
        return (r2.y < r1.y + r1.h && r1.y < r2.y + r2.h
            && r2.x < r1.x + r1.w && r1.x < r2.x + r2.w);
    }
    std::vector<Actor*> actors() { return actors_; }
    Point size() { return {w_, h_}; }
    ~Arena() {
        while (!actors_.empty()) {
            delete actors_.back();
            actors_.pop_back();
        }
    }
};

class BoardGame {
public:
    virtual void play_at(int x, int y) = 0;
    virtual void flag_at(int x, int y) = 0;
    virtual std::string value_at(int x, int y) = 0;
    virtual bool finished() = 0;
    virtual int cols() = 0;
    virtual int rows() = 0;
    virtual std::string message() = 0;

    virtual ~BoardGame() {}
};

void print_game(BoardGame* game) {
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            std::cout << std::setw(3) << game->value_at(x, y);
        }
        std::cout << std::endl;
    }
}

void console_play(BoardGame* game) {
    print_game(game);

    while (! game->finished()) {
        auto x = 0, y = 0;
        std::cout << std::endl << "Move? ";
        std::cin >> x >> y;

        game->play_at(x, y);
        print_game(game);
    }
    std::cout << game->message() << std::endl;
}

bool randomized = false;

int randint(int min, int max) {
    if (!randomized) {
        srand(time(nullptr));
        randomized = true;
    }
    return min + rand() % (1 + max - min);
}

}

std::ostream& operator<<(std::ostream& os, const g2d::Point& p) {
    return os << "Point{" << p.x << ", " << p.y << "}";
}

std::ostream& operator<<(std::ostream& os, const g2d::Rect& r) {
    return os << "Rect{" << r.x << ", " << r.y << ", " << r.w << ", " << r.h << "}";
}

std::ostream& operator<<(std::ostream& os, const g2d::Color& c) {
    return os << "Color{" << c.r << ", " << c.g << ", " << c.b << "}";
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
    os << "[";
    for (int i = 0; i < v.size(); ++i) {
        os << v[i];
        if (i != v.size() - 1) { os << ", "; }
    }
    return os << "]";
}

#endif // ACTOR_HPP
