#include "rightpushbutton.h"
#include <QMouseEvent>

RightPushButton::RightPushButton(QWidget* parent) : QPushButton(parent) {
}

void RightPushButton::mouseReleaseEvent(QMouseEvent* e) {
    if (e->button() == Qt::RightButton)
        emit rightClicked();
    QPushButton::mouseReleaseEvent(e);
}
