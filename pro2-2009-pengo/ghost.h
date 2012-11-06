/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef GHOST_H
#define GHOST_H

#include "actor.h"

class Ghost : public Actor
{
public:
    Ghost(Game* game, int y, int x);
    void move();
    void touchedBy(Actor* other);
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    static const char SYMBOL = '^';
private:
    static const int WAIT = 3;
    int turn;
};

#endif // GHOST_H
