#ifndef SKIER_H
#define SKIER_H

#include "actor.h"

class Skier : public Actor
{
public:
    Skier(int x, int y, int w);

    virtual void move();
    virtual int get_x() { return x_; }
    virtual int get_y() { return y_; }

private:
    int x_;
    int y_;
    int dx_ = 5;
    int dy_ = 5;
    int xmin_;
    int xmax_;
};

#endif // SKIER_H
