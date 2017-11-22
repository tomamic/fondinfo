#include "bouncegui.h"


BounceGui::BounceGui() {
    setFixedSize(320, 240);
    arena_ = new Arena(width(), height());
    new Ball(arena_, 40, 80);
    new Ball(arena_, 80, 40);
    new Ghost(arena_, 60, 60);
    turtle_ = new Turtle(arena_, 80, 80);
    startTimer(1000 / 30);  // 30 fps
}

void BounceGui::timerEvent(QTimerEvent* event) {
    arena_->move_all();
    update();
}

void BounceGui::paintEvent(QPaintEvent* event) {
    QPainter painter{this};
    for (auto a : arena_->actors()) {
        auto pos = a->rect();
        auto sym = a->symbol();
        painter.drawPixmap(pos.x, pos.y, sprites_,
                           sym.x, sym.y, sym.w, sym.h);
    }
}

void BounceGui::keyPressEvent(QKeyEvent* event) {
    auto k = event->key();
    if (k == Qt::Key_Left) {
        turtle_->go_left();
    } else if (k == Qt::Key_Right) {
        turtle_->go_right();
    } else if (k == Qt::Key_Up) {
        turtle_->go_up();
    } else if (k == Qt::Key_Down) {
        turtle_->go_down();
    } else {
        QWidget::keyPressEvent(event);
    }
}

void BounceGui::keyReleaseEvent(QKeyEvent * event) {
    turtle_->stay();
}
