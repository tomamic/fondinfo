#ifndef CAR_H
#define CAR_H

#include "actor.h"

class Car : public Actor
{
public:
    Car(int x, int y, int dx);

    virtual void move();
    virtual int get_x() { return x_; }
    virtual int get_y() { return y_; }

private:
    int x_;
    int y_;
    int dx_;
};

#endif // CAR_H
