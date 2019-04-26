#ifndef BALL_HPP
#define BALL_HPP

class Ball {
    int x_;
    int y_;
    int dx_ = 5;
    int dy_ = 5;

public:
    static const int ARENA_W = 320;
    static const int ARENA_H = 240;
    static const int W = 20;
    static const int H = 20;

    Ball(int x0, int y0) {
        x_ = x0;
        y_ = y0;
    }

    void move() {
        if (x_ + dx_ < 0 || x_ + dx_ + W > ARENA_W) dx_ = -dx_;
        if (y_ + dy_ < 0 || y_ + dy_ + H > ARENA_H) dy_ = -dy_;
        x_ += dx_; y_ += dy_;
    }

    int get_x() {
        return x_;
    }

    int get_y() {
        return y_;
    }
};

#endif // BALL_HPP
