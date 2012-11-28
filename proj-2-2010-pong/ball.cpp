/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
            game->scorePoints(RIGHT, 1);
        } else if (x + dx >= game->getWidth()) {
            dx = -dx;
            game->scorePoints(LEFT, 1);
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
