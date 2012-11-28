/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "ice.h"

Ice::Ice(Game* game, int y, int x) :
    Actor(game, y, x)
{
    dir = STAY;
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
    if (alive && dir >= 0) {
        int newY = y + DY[dir];
        int newX = x + DX[dir];

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
            dir = STAY;
        }
    }
}

void Ice::touchedBy(Actor* other)
{
    // if touched by a player
    if (other->isPlayer()) {
        // find the direction opposite to the player
        dir = 0;
        while (DY[dir] != y - other->getY()
               || DX[dir] != x - other->getX()) {
            ++dir;
        }
        int newY = y + DY[dir];
        int newX = x + DX[dir];

        // if the ice-block is pushed against the border,
        // or against anybody not being an enemy,
        // the ice-block dies
        alive = game->isInside(newY, newX)
                && (game->get(newY, newX) == NULL
                    || game->get(newY, newX)->isEnemy());
    }
}
