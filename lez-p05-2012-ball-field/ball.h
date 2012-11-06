#ifndef BALL_H
#define BALL_H

class Ball
{
public:
    Ball(int x, int y, int dx, int dy,
         int width, int height);
    void move();
    int getX();
    int getY();

private:
    int x;
    int y;
    int dx;
    int dy;
    int width;
    int height;
};

#endif // BALL_H
