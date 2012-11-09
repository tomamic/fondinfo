/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "ice.h"

Ice::Ice(Game* game, int y, int x) :
    Actor(game, y, x),
    direction(STAY)
{
}

bool Ice::isEnemy()
{
    return false;
}

bool Ice::isPlayer()
{
    return false;
}

char Ice::getSymbol()
{
    return SYMBOL;
}

void Ice::move()
{
    if (alive && direction >= 0) {
        int newY = y + DIRECTIONS[direction][DY];
        int newX = x + DIRECTIONS[direction][DX];

        if (game->isInside(newY, newX)) {
            Actor* other = game->get(newY, newX);
            // touch everybody who's in the way
            if (other != NULL) {
                other->touchedBy(this);
            }
            // if the cell is free, eventually, move there
            if (alive && game->get(newY, newX) == NULL) {
                y = newY;
                x = newX;
            }
        }

        if (x != newX || y != newY) {
            direction = STAY;
        }
    }
}

void Ice::touchedBy(Actor* other)
{
    // if touched by a player
    if (other->isPlayer()) {
        // find the direction opposite to the player
        direction = 0;
        while (DIRECTIONS[direction][DY] != y - other->getY()
               || DIRECTIONS[direction][DX] != x - other->getX()) {
            ++direction;
        }
        int newY = y + DIRECTIONS[direction][DY];
        int newX = x + DIRECTIONS[direction][DX];

        // if the ice-block is pushed against the border,
        // or against anybody not being an enemy,
        // the ice-block dies
        alive = game->isInside(newY, newX)
                && (game->get(newY, newX) == NULL
                    || game->get(newY, newX)->isEnemy());
    }
}
