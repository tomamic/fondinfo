/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "penguin.h"

Penguin::Penguin(Game* game, int y, int x) :
    Actor(game, y, x)
{
    game->setCommand(Game::HERO, STAY);
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
    int dir = game->getCommand(Game::HERO);
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
    }
}

void Penguin::touchedBy(Actor* other)
{
    // the penguin dies as soon as it's touched by anybody
    alive = false;
}
