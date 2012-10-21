#include "field.h"

Field::Field(int width, int height) {
    this->width = width;
    this->height = height;
}

Field::~Field() {
    for (int i = 0; i < balls.size(); ++i) {
        Ball* ball = balls[i];
        delete ball;
    }
}

void Field::add(Ball* ball) {
    balls.push_back(ball);
}

void Field::moveAll() {
    for (int i = 0; i < balls.size(); ++i) {
        Ball* ball = balls[i];
        ball->move();
    }
}

char Field::getSymbol(int x, int y) {
    char result = '-';
    for (int i = 0; i < balls.size(); ++i) {
        Ball* ball = balls[i];
        if (x == ball->getX()
                && y == ball->getY()) {
            result = '0' + i;
        }
    }
    return result;
}

void Field::print(std::ostream& out) {
    const char EMPTY = '-';

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            out << getSymbol(x, y);
        }
        out << std::endl;
    }
    out << std::endl;
}
