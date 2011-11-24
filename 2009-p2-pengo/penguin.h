/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef PENGUIN_H
#define PENGUIN_H

#include "actor.h"

class Penguin : public Actor
{
public:
    Penguin(Game* game, int y, int x);
    void move();
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    static const char SYMBOL = '&';
};

#endif // PENGUIN_H
