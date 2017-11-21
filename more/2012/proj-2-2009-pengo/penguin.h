/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef PENGUIN_H
#define PENGUIN_H

#include "actor.h"

class Penguin : public Actor
{
public:
    Penguin(Game* game, int y, int x);
    void move();
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    static const char SYMBOL = '&';
};

#endif // PENGUIN_H
