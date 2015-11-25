#include "car.h"

Car::Car(int x, int y, int dx)
{
    x_ = x;
    y_ = y;
    dx_ = dx;
}

void Car::move()
{
    auto W = 640;
    x_ = (x_ + dx_ + W) % W;
}

