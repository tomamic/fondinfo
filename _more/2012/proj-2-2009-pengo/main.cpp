/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "gamegui.h"
#include "loader.h"
#include "game.h"

#include "ice.h"
#include "ghost.h"
#include "penguin.h"

#include <QtGui/QApplication>
#include <QtCore/QTranslator>
#include <QtCore/QLocale>
#include <cstdlib>
#include <ctime>

int runConsole(int argc, char *argv[])
{
    Game* game = new Game(7, 7);
    new Ice(game, 2, 1);
    new Ice(game, 2, 2);
    new Ice(game, 4, 4);
    new Ice(game, 4, 5);
    new Ghost(game, 0, 3);
    new Ghost(game, 5, 2);
    new Penguin(game, 3, 3);
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
    translator.load(":/translations/pengo_" + QLocale::system().name());
    a.installTranslator(&translator);

    Loader loader(":levels/pengo");
    Game* game = loader.loadGame(1);
    GameGui gui(game);

    return a.exec();
}

int main(int argc, char *argv[])
{
    srand(time(NULL));

    //return runConsole(argc, argv);
    return runGui(argc, argv);
}
