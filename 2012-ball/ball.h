#ifndef BALL_H
#define BALL_H

class Ball
{
    int x;
    int y;
    int dx;
    int dy;

public:
    Ball(int x, int y, int dx, int dy);
    void move();
    int getX();
    int getY();

    static const int WIDTH = 16;
    static const int HEIGHT = 12;
};

#endif // BALL_H
