/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "gamegui.h"
#include "loader.h"
#include "game.h"
#include "autopaddle.h"
#include "ball.h"
#include "paddle.h"

#include <QtGui/QApplication>
#include <QtCore/QTranslator>
#include <QtCore/QLocale>
#include <cstdlib>
#include <ctime>

int runConsole(int argc, char *argv[])
{
    Game* game = new Game(17, 47);
    new Ball(game, 6, 15);
    new Paddle(game, 8, 4, 0);
    new AutoPaddle(game, 8, 0, 2);
    new AutoPaddle(game, 8, 42, 2);
    new AutoPaddle(game, 8, 46, 2);
    game->write(cout);

    while (!game->isLost() && !game->isWon()) {
        string command;
        getline(cin, command);
        if (command == "w") game->setUserCommand(Actor::UP);
        else if (command == "s") game->setUserCommand(Actor::RIGHT);
        else if (command == "z") game->setUserCommand(Actor::DOWN);
        else if (command == "a") game->setUserCommand(Actor::LEFT);
        else game->setUserCommand(Actor::STAY);

        game->moveAll();
        game->write(cout);
    }
    return 0;
}

int runGui(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QTranslator translator;
    translator.load(":/translations/pong_" + QLocale::system().name());
    a.installTranslator(&translator);

    Loader loader(":levels/pong");
    Game* game = loader.loadGame(1);
    GameGui gui(game);

    return a.exec();
}

int main(int argc, char *argv[])
{
    srand(time(NULL));    

//    return runConsole(argc, argv);
    return runGui(argc, argv);
}
