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

int runConsole(QApplication& a)
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
}

int runGui(QApplication& a)
{
    QTranslator translator;
    translator.load(":/translations/pengo_" + QLocale::system().name());
    a.installTranslator(&translator);

    Loader* loader = new Loader(":levels/pengo");
    Game* game = loader->loadGame(1);
    GameGui* w = new GameGui(game);

    return a.exec();
}

int main(int argc, char *argv[])
{
    srand(time(NULL));
    QApplication a(argc, argv);

    //return runConsole(a);
    return runGui(a);

}
