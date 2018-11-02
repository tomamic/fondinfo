#ifndef ACTOR_H
#define ACTOR_H

#include <vector>
#include <algorithm>

using namespace std;

class Actor
{
public:
    virtual void move() = 0;
    virtual void collide(Actor* other) = 0;
    virtual vector<int> position() = 0;
    virtual vector<int> symbol() = 0;
    virtual ~Actor() {}
};

class Arena
{
private:
    int w_, h_;
    vector<Actor*> actors_;
public:
    Arena(int width, int height);
    void add(Actor* a);
    void remove(Actor* a);
    void move_all();
    bool check_collision(Actor* a1, Actor* a2);
    vector<Actor*> actors() { return actors_; }
    vector<int> size() { return {w_, h_}; }
    int width() { return w_; }
    int height() { return h_; }
    ~Arena();
};


#endif // ACTOR_H
