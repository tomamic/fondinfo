#ifndef BALL_H
#define BALL_H

class Ball
{
    int x;
    int y;
    int dx;
    int dy;
    int width;
    int height;

public:
    Ball(int x, int y, int dx, int dy,
         int width, int height);
    void move();
    int getX();
    int getY();
};

#endif // BALL_H
