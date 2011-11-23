#include "gamegui.h"
#include "game.h"

#include <QtGui/QApplication>
#include <QtGui/QGridLayout>
#include <QtGui/QMessageBox>

GameGui::GameGui(Game* game, QWidget* parent) :
    QWidget(parent)
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
    if (key == Qt::Key_Up
            || key == Qt::Key_Right
            || key == Qt::Key_Down
            || key == Qt::Key_Left) {
        game->setUserCommand(Actor::STAY); // PLAYER_1
    } else if (key == Qt::Key_W
               || key == Qt::Key_S
               || key == Qt::Key_Z
               || key == Qt::Key_A) {
        game->setUserCommand(Actor::STAY, PLAYER_2);
    }
    QWidget::keyPressEvent(event);
}
