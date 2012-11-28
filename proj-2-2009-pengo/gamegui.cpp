/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "gamegui.h"
#include "game.h"

#include <QtGui/QApplication>
#include <QtGui/QGridLayout>
#include <QtGui/QMessageBox>

GameGui::GameGui(Game* game)
{
    setWindowTitle(tr("Pengo"));
    this->game = game;
    QGridLayout* layout = new QGridLayout();
    layout->setSpacing(0);
    layout->setSizeConstraint(QLayout::SetFixedSize);
    for (int y = 0; y < game->getHeight(); ++y) {
        for (int x = 0; x < game->getWidth(); ++x) {
            QLabel* l = new QLabel();
            l->setFixedSize(20, 20);
            layout->addWidget(l, y, x);
            labels.push_back(l);
        }
    }
    updateAllLabels();

    this->setLayout(layout);
    adjustSize();

    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(updateGame()));
    timer->start(100);
    show();
}

void GameGui::updateGame()
{
    if (game->isLost()) {
        QMessageBox::information(this, tr("Game lost!"), tr("Game lost!"));
        qApp->quit();
    } else if (game->isWon()) {
        QMessageBox::information(this, tr("Game won!"), tr("Game won!"));
        qApp->quit();
    } else {
        game->moveAll();
        updateAllLabels();
    }
}

void GameGui::updateAllLabels()
{
    for (int y = 0; y < game->getHeight(); ++y) {
        for (int x = 0; x < game->getWidth(); ++x) {
            Actor* a = game->get(y, x);
            char symbol = ' ';
            if (a != NULL) symbol = a->getSymbol();
            int i = y * game->getWidth() + x;
            labels[i]->setText(QString(symbol));
        }
    }
}

void GameGui::keyPressEvent(QKeyEvent* event)
{
    int key = event->key();
    if (key == Qt::Key_Up) {
        game->setCommand(Game::HERO, Actor::UP);
    } else if (key == Qt::Key_Right) {
        game->setCommand(Game::HERO, Actor::RIGHT);
    } else if (key == Qt::Key_Down) {
        game->setCommand(Game::HERO, Actor::DOWN);
    } else if (key == Qt::Key_Left) {
        game->setCommand(Game::HERO, Actor::LEFT);
    } else if (key == Qt::Key_W) {
        game->setCommand(Game::HERO + 1, Actor::UP);
    } else if (key == Qt::Key_S) {
        game->setCommand(Game::HERO + 1, Actor::RIGHT);
    } else if (key == Qt::Key_Z) {
        game->setCommand(Game::HERO + 1, Actor::DOWN);
    } else if (key == Qt::Key_A) {
        game->setCommand(Game::HERO + 1, Actor::LEFT);
    }
    QWidget::keyPressEvent(event);
}

void GameGui::keyReleaseEvent(QKeyEvent* event)
{
    int key = event->key();
    if (key == Qt::Key_Up
            || key == Qt::Key_Right
            || key == Qt::Key_Down
            || key == Qt::Key_Left) {
        game->setCommand(Game::HERO, Actor::STAY);
    } else if (key == Qt::Key_W
               || key == Qt::Key_S
               || key == Qt::Key_Z
               || key == Qt::Key_A) {
        game->setCommand(Game::HERO + 1, Actor::STAY);
    }
    QWidget::keyPressEvent(event);
}
