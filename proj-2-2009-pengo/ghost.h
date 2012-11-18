/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef GHOST_H
#define GHOST_H

#include "actor.h"

class Ghost : public Actor
{
public:
    Ghost(Game* game, int y, int x);
    void move();
    void touchedBy(Actor* other);
    char getSymbol();
    bool isEnemy();
    bool isPlayer();
    static const char SYMBOL = '^';
private:
    static const int WAIT = 3;
    int turn;
};

#endif // GHOST_H
