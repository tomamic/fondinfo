/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
                // if the ball is close enough, follow it
                if (a->getY() < middle) command = UP;
                else if (a->getY() > middle) command = DOWN;
            } else {
                // otherwise, move to closer the center
                if (middle > 0.66 * game->getHeight()) command = UP;
                else if (middle < 0.33 * game->getHeight()) command = DOWN;
            }
        }

        ++i;
        a = game->getActor(i);
    }

    game->setCommand(id, command);
    Paddle::move();
}
