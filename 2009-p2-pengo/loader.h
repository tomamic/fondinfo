/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2009
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef LOADER_H
#define LOADER_H

#include "game.h"

using namespace std;

class Loader
{
public:
    Loader(string name);
    Game* loadGame(int level);
private:
    string name;
};

#endif // LOADER_H
