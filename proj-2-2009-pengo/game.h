/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
    Actor* getActor(int i);
    int getHeight();
    int getWidth();
    bool isWon();
    bool isLost();
    bool isInside(int y, int x);
    void write(ostream& out);
    int getCommand(int player);
    void setCommand(int player, int command);
    void setNextCommand(int player, int command);
    void updateCommands();
    int getPoints(int player);
    void scorePoints(int player, int points);

    static const char BLANK = '.';
    static const int HERO = 0;

private:
    int height;
    int width;
    vector<Actor*> actors;
    map<int, int> commands;
    map<int, int> points;
    vector< pair<int, int> > nextCommands;

    // In fact, a matrix is not required
    // ... but it would improve performance
    // Actor* map[MAX_HEIGHT][MAX_WIDTH];
};

#endif // GAME_H
