/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef BALL_H
#define BALL_H

#include "actor.h"

class Ball : public Actor
{
public:
    Ball(Game* level, int y, int x);
    void move();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    char getSymbol();
    static const char SYMBOL = '*';

private:
    int dx;
    int dy;
};

#endif // BALL_H
