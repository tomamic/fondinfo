/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
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
    return (alive && this->x == x
            && this->y <= y && y < (this->y + length));
}

void Paddle::move()
{
    int dir = game->getUserCommand(id);
    if (alive && (dir == UP || dir == DOWN)) {
        int newY = (dir == UP) ? (y - 1) : (y + length);

        if (game->isInside(newY, x)) {
            Actor* other = game->get(newY, x);
            // touch everybody who's in the way
            if (other != NULL && other != this) {
                other->touchedBy(this);
            }

            // if the cell is free, eventually, move there
            other = game->get(newY, x);
            if (alive && (other == NULL || other == this)) {
                y = y + DY[dir];
            }
        }
    }
}

void Paddle::touchedBy(Actor* other)
{
}
