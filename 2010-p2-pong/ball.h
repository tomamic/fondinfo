/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef BALL_H
#define BALL_H

#include "actor.h"

class Ball : public Actor
{
public:
    Ball(Game* level, int y, int x);
    void move();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    char getSymbol();
    static const char SYMBOL = '*';

private:
    int dx;
    int dy;
};

#endif // BALL_H
