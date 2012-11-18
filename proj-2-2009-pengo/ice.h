/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef ICE_H
#define ICE_H

#include "actor.h"

class Ice : public Actor
{
public:
    Ice(Game* game, int y, int x);
    void move();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    char getSymbol();
    static const char SYMBOL = '#';
private:
    int dir;
};

#endif // ICE_H
