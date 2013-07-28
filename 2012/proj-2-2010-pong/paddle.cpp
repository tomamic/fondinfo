/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "paddle.h"

Paddle::Paddle(Game* game, int y, int x, int id)
    : Actor(game, y, x)
{
    this->id = id;
    length = INITIAL_LENGTH;
    game->setCommand(id, STAY);
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
    int dir = game->getCommand(id);
    if (alive && (dir == UP || dir == DOWN)) {
        int newY = y + length;
        if (dir == UP) newY = y - 1;

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
