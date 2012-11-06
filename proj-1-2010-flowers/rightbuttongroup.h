/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef RIGHTBUTTONGROUP_H
#define RIGHTBUTTONGROUP_H

#include <QButtonGroup>

class RightButtonGroup : public QButtonGroup
{
    Q_OBJECT

public:
    RightButtonGroup(QObject* parent = NULL);
    void addButton(QAbstractButton* button, int id);

signals:
    void buttonRightClicked(int id);
    void buttonRightClicked(QAbstractButton* button);

private slots:
    void emitRightClicked();
};

#endif // RIGHTBUTTONGROUP_H
