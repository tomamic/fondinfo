/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "autopaddle.h"

#include <cstdlib>

AutoPaddle::AutoPaddle(Game* game, int y, int x, int id)
    : Paddle(game, y, x, id)
{
}

void AutoPaddle::move()
{
    int command = STAY;
    int middle = y + (length / 2);

    int i = 0;
    Actor* a = game->getActor(i);
    while (a != NULL) {
        if (a->isEnemy()) {
            if (abs(a->getX() - x) < 0.5 * game->getHeight()) {
                if (a->getY() < middle) command = UP;
                else if (a->getY() > middle) command = DOWN;
            } else {
                if (middle > 0.66 * game->getHeight()) command = UP;
                else if (middle < 0.33 * game->getHeight()) command = DOWN;
            }
        }

        ++i;
        a = game->getActor(i);
    }

    game->setUserCommand(command, id);
    Paddle::move();
}
