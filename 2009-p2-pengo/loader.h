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
