/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef GAME_H
#define GAME_H

#include "actor.h"

#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Actor;

class Game
{
public:
    Game(int height, int width);
    ~Game();
    void addActor(Actor* actor);
    void moveAll();
    Actor* get(int y, int x);
    //void set(int y, int x, Actor* actor);
    int getHeight();
    int getWidth();
    bool isWon();
    bool isLost();
    bool isInside(int y, int x);
    void write(ostream& out);
    int getUserCommand(int player = 0);
    void setUserCommand(int command, int player = 0);

    static const char BLANK = '.';
private:
    int height;
    int width;
    vector<Actor*> actors;
    map<int, int> commands;

    // In fact, a matrix is not required
    // ... but it would improve performance
    // Actor* map[MAX_HEIGHT][MAX_WIDTH];
};

#endif // GAME_H
