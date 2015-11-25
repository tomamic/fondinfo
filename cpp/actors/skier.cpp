#include "skier.h"

Skier::Skier(int x, int y, int w)
{
    x_ = x;
    y_ = y;
    xmin_ = x;
    xmax_ = x + w;
}

void Skier::move()
{
    auto H = 480;
    if (xmin_ > x_ + dx_ || x_ + dx_ >= xmax_) {
        dx_ = -dx_;
    }
    x_ += dx_;
    y_ += dy_;
    if (y_ > H) y_ = 0;
}

