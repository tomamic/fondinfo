/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef NOTEPAD_H
#define NOTEPAD_H

#include <QtGui/QMainWindow>
#include <QtGui/QTextEdit>

class Notepad : public QMainWindow
{
    Q_OBJECT

public:
    Notepad(QWidget* parent = 0);
    ~Notepad();

private slots:
    void open();
    void save();
    void exit();

private:
    QTextEdit* textEdit;
};

#endif // NOTEPAD_H
