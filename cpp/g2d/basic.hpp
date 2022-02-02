/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef ACTOR_HPP
#define ACTOR_HPP

#include <algorithm>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <regex>
#include <set>
#include <string>
#include <vector>

namespace g2d {

struct Point {
    int x, y;
    Point(int x0, int y0) { x=x0; y=y0; }
    int __getitem__(int i) { return i==0 ? x : y; }
    int __len__() { return 2; }
};
struct Color {
    int r, g, b;
    Color(int r0, int g0, int b0) { r=r0; g=g0; b=b0; }
    int __getitem__(int i) { return i==0 ? r : i==1 ? g : b; }
    int __len__() { return 3; }
};

class Arena;

class Actor {
public:
    virtual void move(Arena* arena) = 0;
    virtual void collide(Actor* other, Arena* arena) = 0;
    virtual Point pos() = 0;
    virtual Point size() = 0;
    virtual Point sprite() = 0;
    virtual ~Actor() {}
};

class Arena {
private:
    int w_, h_, count_;
    std::vector<Actor*> actors_;
    std::vector<Actor*> spawned_;
    std::vector<Actor*> killed_;
    std::set<std::string> current_keys_;
    std::set<std::string> previous_keys_;
public:
    Arena(Point size) { w_ = size.x; h_ = size.y; count_ = 0; }
    void spawn(Actor* a) {
        spawned_.push_back(a);
    }
    void kill(Actor* a) {
        killed_.push_back(a);
    }
    void tick(std::set<std::string> keys={}) {
        previous_keys_ = current_keys_;
        current_keys_ = keys;

        auto acts = actors();
        reverse(begin(acts), end(acts));
        for (auto a : acts) {
            a->move(this);
            for (auto other : acts) {
                if (check_collision(a, other)) {
                    a->collide(other, this);
                }
            }
        }

        actors_.insert(actors_.end(), spawned_.begin(), spawned_.end());
        spawned_.clear();
        for (auto a : killed_) {
            auto pos = find(begin(actors_), end(actors_), a);
            if (pos != end(actors_)) { actors_.erase (pos); }
        }
        killed_.clear();
        count_++;
    }
    bool check_collision(Actor* a1, Actor* a2) {
        auto p1 = a1->pos(), s1 = a1->size();
        auto p2 = a2->pos(), s2 = a2->size();
        return (a1 != a2 && p2.y < p1.y + s1.y && p1.y < p2.y + s2.y
            && p2.x < p1.x + s1.x && p1.x < p2.x + s2.x);
    }
    std::vector<Actor*> actors() { return actors_; }
    Point size() { return {w_, h_}; }
    ~Arena() {
        while (!actors_.empty()) {
            delete actors_.back();
            actors_.pop_back();
        }
    }
    std::set<std::string> current_keys() { return current_keys_; }
    std::set<std::string> previous_keys() { return previous_keys_; }
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

std::vector<std::string> split(const std::string& text, const std::string& sep) {
    auto result = std::vector<std::string>{};
    auto re = std::regex{sep};
    copy(std::sregex_token_iterator(text.begin(), text.end(), re, -1),
         std::sregex_token_iterator(), std::back_inserter(result));
    return result;
}

}  // namespace g2d


std::string to_stream(const g2d::Point& p) {
    return std::string{"Point{"} + std::to_string(p.x) + ", " + std::to_string(p.y) + "}";
}

std::string to_stream(const g2d::Color& c) {
    return std::string{"Color{"} + std::to_string(c.r) + ", " + std::to_string(c.g) + ", " + std::to_string(c.b) + "}";
}

template <typename T>
std::string to_string(const std::vector<T>& v) {
    std::string result = "[";
    for (int i = 0; i < v.size(); ++i) {
        if (i) { result += ", "; }
        result += std::to_string(v[i]);
    }
    return result + "]";
}

std::ostream& operator<<(std::ostream& os, const g2d::Point& p) {
    return os << "Point{" << p.x << ", " << p.y << "}";
}

std::ostream& operator<<(std::ostream& os, const g2d::Color& c) {
    return os << "Color{" << c.r << ", " << c.g << ", " << c.b << "}";
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
    os << "[";
    for (int i = 0; i < v.size(); ++i) {
        if (i) { os << ", "; }
        os << v[i];
    }
    return os << "]";
}

#endif // ACTOR_HPP
