/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
