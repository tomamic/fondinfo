#ifndef BOUNCE_H
#define BOUNCE_H

#include "actor.h"
#include <vector>

using namespace std;

class Ghost : public Actor
{
private:
    Arena* arena_;
    int x_, y_;
    bool visible_ = true;
    static const int W = 20, H = 20, SPEED = 5;
public:
    Ghost(Arena* arena, int x, int y);
    void move();
    void collide(Actor* other);
    vector<int> position();
    vector<int> symbol();
};


class Ball : public Actor
{
private:
    Arena* arena_;
    int x_, y_, dx_, dy_;
    static const int W = 20, H = 20, SPEED = 5;
public:
    Ball(Arena* arena, int x, int y);
    void move();
    void collide(Actor* other);
    vector<int> position();
    vector<int> symbol();
};


class Turtle : public Actor
{
private:
    Arena* arena_;
    int x_, y_, dx_, dy_;
    static const int W = 20, H = 20, SPEED = 2;
public:
    Turtle(Arena* arena, int x, int y);
    void move();
    void collide(Actor* other);
    vector<int> position();
    vector<int> symbol();
    void go_left();
    void go_right();
    void go_up();
    void go_down();
    void stay();
};


#endif // BOUNCE_H
