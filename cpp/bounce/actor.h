#ifndef ACTOR_H
#define ACTOR_H

#include <vector>
#include <algorithm>

using namespace std;

struct Rect
{
    int x, y, w, h;
};

class Actor
{
public:
    virtual void move() = 0;
    virtual void collide(Actor* other) = 0;
    virtual Rect rect() = 0;
    virtual Rect symbol() = 0;
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
    vector<Actor*> actors();
    Rect rect();
};


#endif // ACTOR_H
