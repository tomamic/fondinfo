/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "ball.h"

Ball::Ball(Game* level, int y, int x)
    : Actor(level, y, x)
{
    dy = 1;
    dx = 1;
}

bool Ball::isEnemy()
{
    return true;
}

bool Ball::isPlayer()
{
    return false;
}

char Ball::getSymbol()
{
    return SYMBOL;
}

void Ball::move()
{
    if (alive) {
        if (y + dy < 0 || y + dy >= game->getHeight()) {
            dy = -dy;
        }

        if (x + dx < 0) {
            dx = -dx;
            game->scorePoints(1, RIGHT);
        } else if (x + dx >= game->getWidth()) {
            dx = -dx;
            game->scorePoints(1, LEFT);
        }

        Actor* other = game->get(y + dy, x + dx);
        // touch everybody who's in the way
        if (other != NULL) {
            other->touchedBy(this);
            dx = -dx;
        }
        x += dx;
        y += dy;
    }
}

void Ball::touchedBy(Actor* other)
{
}
