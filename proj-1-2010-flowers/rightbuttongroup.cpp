/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
