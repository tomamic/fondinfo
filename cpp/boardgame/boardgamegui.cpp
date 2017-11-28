/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "boardgamegui.h"

#include <QGridLayout>
#include <QMessageBox>
#include <QPushButton>
#include <QVariant>

BoardGameGui::BoardGameGui(BoardGame* g)
{
    game = g;
    auto grid = new QGridLayout;
    setLayout(grid);
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            auto b = new QPushButton;
            b->setFixedSize(25, 25);
            grid->addWidget(b, y, x);
            // lambda function; closure captures this, x, y
            connect(b, &QPushButton::clicked, [=]{
                game->play_at(x, y);
                update_buttons();
            });
        }
    }
    update_buttons();

    // fix appearance
    layout()->setMargin(0);
    layout()->setSpacing(0);
}

void BoardGameGui::update_buttons()
{
    for (auto y = 0; y < game->rows(); ++y) {
        for (auto x = 0; x < game->cols(); ++x) {
            auto val = game->get_val(x, y).c_str();
            auto i = y * game->cols() + x;
            auto b = layout()->itemAt(i)->widget();
            b->setProperty("text", val);
        }
    }
    if (game->finished()) {
        auto msg = game->message().c_str();
        QMessageBox::information(this, tr("Game finished"), tr(msg));
        window()->close();
    }
}
