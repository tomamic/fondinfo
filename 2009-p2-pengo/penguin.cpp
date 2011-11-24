/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "penguin.h"

Penguin::Penguin(Game* game, int y, int x) :
    Actor(game, y, x)
{
    game->setUserCommand(STAY);
}

char Penguin::getSymbol()
{
    return SYMBOL;
}

bool Penguin::isEnemy()
{
    return false;
}

bool Penguin::isPlayer()
{
    return true;
}

void Penguin::move()
{
    int direction = game->getUserCommand();
    if (alive && direction >= 0) {
        int newY = y + DY[direction];
        int newX = x + DX[direction];

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
    }
}

void Penguin::touchedBy(Actor* other)
{
    // the penguin dies as soon as it's touched by anybody
    alive = false;
}
