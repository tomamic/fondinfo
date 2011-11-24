/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef RIGHTPUSHBUTTON_H
#define RIGHTPUSHBUTTON_H

#include <QPushButton>

class RightPushButton : public QPushButton
{
    Q_OBJECT

public:
    RightPushButton(QWidget* parent = NULL);

protected:
    void mouseReleaseEvent(QMouseEvent* e);

signals:
    void rightClicked();
};

#endif // RIGHTPUSHBUTTON_H
