/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
