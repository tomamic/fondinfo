/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef NOTEPAD_H
#define NOTEPAD_H

#include <QtGui/QMainWindow>
#include <QtGui/QTextEdit>


class Notepad : public QWidget
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
