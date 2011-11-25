/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "gamegui.h"
#include "game.h"

#include <QtGui/QApplication>
#include <QtGui/QGridLayout>
#include <QtGui/QMessageBox>

GameGui::GameGui(Game* game, QWidget* parent)
    : QWidget(parent)
{
    setWindowTitle(tr("Pong"));
    this->game = game;

    QHBoxLayout* pointsLayout = new QHBoxLayout();
    points1 = new QLCDNumber();
    points2 = new QLCDNumber();
    pointsLayout->addWidget(points1);
    pointsLayout->addStretch();
    pointsLayout->addWidget(points2);

    QGridLayout* tableLayout = new QGridLayout();
    tableLayout->setSpacing(0);
    tableLayout->setSizeConstraint(QLayout::SetFixedSize);
    for (int y = 0; y < game->getHeight(); ++y) {
        for (int x = 0; x < game->getWidth(); ++x) {
            QLabel* l = new QLabel();
            l->setFixedSize(20, 20);
            tableLayout->addWidget(l, y, x);
            labels.push_back(l);
        }
    }
    updateAllLabels();

    QVBoxLayout* allLayout = new QVBoxLayout();
    allLayout->addLayout(pointsLayout);
    allLayout->addLayout(tableLayout);
    this->setLayout(allLayout);
    adjustSize();

    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(updateGame()));
    timer->start(100);
    show();
}

void GameGui::updateGame()
{
    points1->display(game->getPoints(Actor::LEFT));
    points2->display(game->getPoints(Actor::RIGHT));
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
            char symbol = (a != NULL) ? a->getSymbol() : ' ';
            int i = y * game->getWidth() + x;
            labels[i]->setText(QString(symbol));
        }
    }
}

void GameGui::keyPressEvent(QKeyEvent* event)
{
    int key = event->key();
    if (key == Qt::Key_Up) {
        game->setUserCommand(Actor::UP); // PLAYER_1
    } else if (key == Qt::Key_Right) {
        game->setUserCommand(Actor::RIGHT); // PLAYER_1
    } else if (key == Qt::Key_Down) {
        game->setUserCommand(Actor::DOWN); // PLAYER_1
    } else if (key == Qt::Key_Left) {
        game->setUserCommand(Actor::LEFT); // PLAYER_1
    } else if (key == Qt::Key_W) {
        game->setUserCommand(Actor::UP, PLAYER_2);
    } else if (key == Qt::Key_S) {
        game->setUserCommand(Actor::RIGHT, PLAYER_2);
    } else if (key == Qt::Key_Z) {
        game->setUserCommand(Actor::DOWN, PLAYER_2);
    } else if (key == Qt::Key_A) {
        game->setUserCommand(Actor::LEFT, PLAYER_2);
    }
    QWidget::keyPressEvent(event);
}

void GameGui::keyReleaseEvent(QKeyEvent* event)
{
    int key = event->key();
    if (key == Qt::Key_Up || key == Qt::Key_Right || key == Qt::Key_Down || key == Qt::Key_Left) {
        game->setUserCommand(Actor::STAY); // PLAYER_1
    } else if (key == Qt::Key_W || key == Qt::Key_S || key == Qt::Key_Z || key == Qt::Key_A) {
        game->setUserCommand(Actor::STAY, PLAYER_2);
    }
    QWidget::keyPressEvent(event);
}
