#ifndef NOTEPAD_H
#define NOTEPAD_H

#include <QWidget>
#include <QTextEdit>
#include <QPushButton>

class Notepad : public QWidget {
    Q_OBJECT
    
public:
    Notepad();
    ~Notepad();

    // slots, to connect with signals
    void open();
    void save();
    void exit();

private:
    QTextEdit* text_edit = new QTextEdit;
    QPushButton* open_button = new QPushButton{tr("&Open")};
    QPushButton* save_button = new QPushButton{tr("&Save")};
    QPushButton* exit_button = new QPushButton{tr("E&xit")};
};

#endif // NOTEPAD_H
