/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
