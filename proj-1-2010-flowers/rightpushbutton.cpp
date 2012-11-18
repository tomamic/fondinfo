/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
