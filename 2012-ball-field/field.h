#ifndef FIELD_H
#define FIELD_H

#include "ball.h"

#include <iostream>
#include <vector>

class Field
{
    int width;
    int height;
    std::vector<Ball*> balls;
    char getSymbol(int x, int y);

public:
    Field(int width, int height);
    ~Field();

    void add(Ball* ball);
    void moveAll();
    void print(std::ostream& out);
};

#endif // FIELD_H
