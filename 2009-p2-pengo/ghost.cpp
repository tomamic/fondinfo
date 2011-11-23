#include "ghost.h"
#include "penguin.h"
#include "ice.h"
#include <cstdlib>

Ghost::Ghost(Game* game, int y, int x) :
    Actor(game, y, x),
    turn(0)
{
}

char Ghost::getSymbol()
{
    return SYMBOL;
}

bool Ghost::isEnemy()
{
    return true;
}

bool Ghost::isPlayer()
{
    return false;
}

void Ghost::move()
{
    ++turn;
    if (alive && (turn % WAIT == 0)) {
        int direction = 2 * (rand() % DIRECTIONS);
        int newY = y + DY[direction];
        int newX = x + DX[direction];

        if (game->isInside(newY, newX)) {
            Actor* other = game->get(newY, newX);
            // don't touch anybody... but players
            if (other != NULL && other->isPlayer()) {
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

void Ghost::touchedBy(Actor* other)
{
    // if a player touches a ghost, the player dies
    // otherwise, the ghost dies
    if (other->isPlayer()) {
        other->touchedBy(this);
    } else {
        alive = false;
    }
}
