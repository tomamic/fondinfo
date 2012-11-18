/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef ACTOR_H
#define ACTOR_H

#include <vector>

#include "game.h"

class Game;

class Actor
{
public:
    Actor(Game* level, int y, int x);
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
    static const int UP_RIGHT = 1;
    static const int RIGHT = 2;
    static const int DOWN_RIGHT = 3;
    static const int DOWN = 4;
    static const int DOWN_LEFT = 5;
    static const int LEFT = 6;
    static const int UP_LEFT = 7;

protected:
    Game* game;
    int y;
    int x;
    int z;
    bool alive;

    static const int NUM_DIRS = 8;
    static const int DY[];
    static const int DX[];
};

#endif // ACTOR_H
