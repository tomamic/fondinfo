/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "paddle.h"

Paddle::Paddle(Game* game, int y, int x, int id)
    : Actor(game, y, x)
{
    this->id = id;
    length = INITIAL_LENGTH;
    game->setUserCommand(STAY, id);
}

char Paddle::getSymbol()
{
    return SYMBOL;
}

bool Paddle::isEnemy()
{
    return false;
}

bool Paddle::isPlayer()
{
    return true;
}

bool Paddle::isAt(int y, int x)
{
    return (alive && this->y <= y && y < (this->y + length) && this->x == x);
}

void Paddle::move()
{
    int direction = game->getUserCommand(id);
    if (alive && (direction == UP || direction == DOWN)) {
        int newY = direction == UP ? (y - 1) : (y + length);

        if (game->isInside(newY, x)) {
            Actor* other = game->get(newY, x);
            // touch everybody who's in the way
            if (other != NULL && other != this) {
                other->touchedBy(this);
            }

            // if the cell is free, eventually, move there
            other = game->get(newY, x);
            if (alive && (other == NULL || other == this)) {
                y = y + DY[direction];
            }
        }
    }
}

void Paddle::touchedBy(Actor* other)
{
}
