/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "rightpushbutton.h"
#include <QMouseEvent>

RightPushButton::RightPushButton(QWidget* parent) : QPushButton(parent) {
}

void RightPushButton::mouseReleaseEvent(QMouseEvent* e) {
    if (e->button() == Qt::RightButton)
        emit rightClicked();
    QPushButton::mouseReleaseEvent(e);
}
