/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
    new Paddle(game, 8, 4, Game::HERO);
    new AutoPaddle(game, 8, 0, 2);
    new AutoPaddle(game, 8, 42, 2);
    new AutoPaddle(game, 8, 46, 2);
    game->write(cout);

    string command;
    getline(cin, command);
    while (cin.good() && !game->isLost() && !game->isWon()) {
        if (command == "w") game->setCommand(Game::HERO, Actor::UP);
        else if (command == "s") game->setCommand(Game::HERO, Actor::RIGHT);
        else if (command == "z") game->setCommand(Game::HERO, Actor::DOWN);
        else if (command == "a") game->setCommand(Game::HERO, Actor::LEFT);
        else game->setCommand(Game::HERO, Actor::STAY);

        game->moveAll();
        game->write(cout);

        if (!game->isLost() && !game->isWon()) {
            getline(cin, command);
        }
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

    return runGui(argc, argv);
//    return runConsole(argc, argv);
}
