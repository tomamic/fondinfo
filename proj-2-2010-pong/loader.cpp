/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "loader.h"
#include "game.h"
#include "ball.h"
#include "paddle.h"
#include "autopaddle.h"

#include <fstream>
#include <sstream>
#include <QtCore/QFile>
#include <QtCore/QTextStream>

using namespace std;

Loader::Loader(string name)
{
    this->name = name;
}

Game* Loader::loadGame(int level)
{
    QFile file(QString("%1-%2.dat").arg(name.c_str()).arg(level));
    file.open(QIODevice::ReadOnly | QIODevice::Text);
    istringstream in(file.readAll().data());

    int h, w, y, x;
    char type;

    in >> h >> w;
    Game* game = new Game(h, w);

    in >> type >> y >> x;
    while (in.good()) {
        if (type == Ball::SYMBOL) {
            new Ball(game, y, x);
        } else if ('0' <= type && type <= '9') {
            new Paddle(game, y, x, type - '0');
        } else if ('A' <= type && type <= 'Z') {
            new AutoPaddle(game, y, x, type);
        }
        in >> type >> y >> x;
    }
    return game;
}
