/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "rightbuttongroup.h"
#include "rightpushbutton.h"

RightButtonGroup::RightButtonGroup(QObject* parent) : QButtonGroup(parent) {
}

void RightButtonGroup::addButton(QAbstractButton* button, int id) {
	RightPushButton* rb = dynamic_cast<RightPushButton*>(button);
    if (rb != NULL) {
		connect(rb, SIGNAL(rightClicked()), this, SLOT(emitRightClicked()));
	}
    QButtonGroup::addButton(button, id);
}

void RightButtonGroup::emitRightClicked() {
    QAbstractButton* button = dynamic_cast<QAbstractButton*>(sender());
    emit buttonRightClicked(button);
    emit buttonRightClicked(id(button));
}
