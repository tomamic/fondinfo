#ifndef BALL_H
#define BALL_H

#include <string>

class Ball {
public:
    Ball(int x0, int y0);
    void move();
    int get_x();
    int get_y();

    static const int ARENA_W = 320;
    static const int ARENA_H = 240;
    static const int W = 20; static const int H = 20;

private:
    int x;
    int y;
    int dx = 5;
    int dy = 5;
};

#endif // BALL_H
