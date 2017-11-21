/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "game.h"

using namespace std;

Game::Game(int height, int width)
{
    this->height = height;
    this->width = width;
}

Game::~Game()
{
    while (actors.size() > 0) {
        delete actors.back();
        actors.pop_back();
    }
}

int Game::getHeight()
{
    return height;
}

int Game::getWidth()
{
    return width;
}

bool Game::isInside(int y, int x)
{
    return 0 <= y && y < height && 0 <= x && x < width;
}

Actor* Game::get(int y, int x)
{
    Actor* result = NULL;
    if (isInside(y, x)) {
        for (int i = 0; i < actors.size(); ++i) {
            Actor* a = actors[i];
            if (a->isAt(y, x)
                    && (result == NULL
                        || result->getZ() < a->getZ())) {
                result = a;
            }
        }
    }
    return result;
}

void Game::addActor(Actor* actor)
{
    actors.push_back(actor);
}

Actor* Game::getActor(int i)
{
    return (0 <= i && i < actors.size()) ? actors[i] : NULL;
}

int Game::getCommand(int player)
{
    return commands[player];
}

void Game::setCommand(int player, int command)
{
    this->commands[player] = command;
}

void Game::setNextCommand(int player, int command)
{
    nextCommands.push_back(pair<int, int>(player, command));
}

void Game::updateCommands()
{
    for (int i = 0; i < nextCommands.size(); ++i) {
        setCommand(nextCommands[i].first, nextCommands[i].second);
    }
    nextCommands.clear();
}

int Game::getPoints(int player)
{
    return points[player];
}

void Game::scorePoints(int player, int points)
{
    this->points[player] += points;
}

void Game::moveAll()
{
    updateCommands();

    for (int i = 0; i < actors.size(); ++i) {
        if (actors[i]->isAlive()) {
            actors[i]->move();
        }
    }
}

bool Game::isWon()
{
    bool won = true;
    for (int i = 0; i < actors.size() && won; ++i) {
        if (actors[i]->isEnemy() && actors[i]->isAlive()) {
            won = false;
        }
    }
    return won;
}

bool Game::isLost()
{
    bool lost = true;
    for (int i = 0; i < actors.size(); ++i) {
        if (actors[i]->isPlayer() && actors[i]->isAlive()) {
            lost = false;
        }
    }
    return lost;
}

void Game::write(ostream& out)
{
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            Actor* a = get(y, x);
            if (a == NULL) { out << BLANK; }
            else { out << a->getSymbol(); }
        }
        out << endl;
    }
}
