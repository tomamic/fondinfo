/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef PADDLE_H
#define PADDLE_H

#include "actor.h"

class Paddle : public Actor
{
public:
    Paddle(Game* level, int y, int x, int id);
    void move();
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    bool isAt(int y, int x);
    void touchedBy(Actor* other);
    static const char SYMBOL = '+';

protected:
    static const int INITIAL_LENGTH = 3;
    int length;
    int id;
};

#endif // PADDLE_H
