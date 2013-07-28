#ifndef NOTEPAD_H
#define NOTEPAD_H

#include <QWidget>
#include <QTextEdit>
#include <QPushButton>

class Notepad : public QWidget
{
    Q_OBJECT
    
public:
    Notepad(QWidget *parent = 0);
    ~Notepad();

public slots:   // special methods, to connect with signals
    void open();
    void save();
    void exit();

private:
    QTextEdit* textEdit;
    QPushButton* openButton;
    QPushButton* saveButton;
    QPushButton* exitButton;
};

#endif // NOTEPAD_H
