/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "actor.h"

const int Actor::DY[] = {-1,  0, +1,  0};
const int Actor::DX[] = { 0, +1,  0, -1};

Actor::Actor(Game* game, int y, int x)
{
    this->game = game;
    this->y = y;
    this->x = x;
    alive = true;
    game->addActor(this);
}

void Actor::setX(int x)
{
    this->x = x;
}

int Actor::getX()
{
    return x;
}

void Actor::setY(int y)
{
    this->y = y;
}

int Actor::getY()
{
    return y;
}

void Actor::setZ(int z)
{
    this->z = z;
}

int Actor::getZ()
{
    return z;
}

bool Actor::isAt(int y, int x)
{
    return (alive && this->y == y && this->x == x);
}

bool Actor::isAlive()
{
    return alive;
}
