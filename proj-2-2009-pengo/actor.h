/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef ACTOR_H
#define ACTOR_H

#include <vector>

#include "game.h"

class Game;

class Actor
{
public:
    Actor(Game* game, int y, int x);
    virtual int getX();
    virtual int getY();
    virtual int getZ();
    virtual void setX(int x);
    virtual void setY(int y);
    virtual void setZ(int z);
    virtual bool isAt(int y, int x);
    virtual bool isAlive();

    virtual char getSymbol() = 0;
    virtual bool isEnemy() = 0;
    virtual bool isPlayer() = 0;
    virtual void move() = 0;
    virtual void touchedBy(Actor* other) = 0;

    static const int STAY = -1;
    static const int UP = 0;
    static const int RIGHT = 1;
    static const int DOWN = 2;
    static const int LEFT = 3;

protected:
    Game* game;
    int y;
    int x;
    int z;
    bool alive;

    static const int DY = 0;
    static const int DX = 1;
    static const std::vector< std::vector<int> > DIRECTIONS;
};

#endif // ACTOR_H
