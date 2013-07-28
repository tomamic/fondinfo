/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef PADDLE_H
#define PADDLE_H

#include "actor.h"

class Paddle : public Actor
{
public:
    Paddle(Game* level, int y, int x, int id);
    void move();
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    bool isAt(int y, int x);
    void touchedBy(Actor* other);
    static const char SYMBOL = '+';

protected:
    static const int INITIAL_LENGTH = 3;
    int length;
    int id;
};

#endif // PADDLE_H
