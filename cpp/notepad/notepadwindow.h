#ifndef NOTEPADWINDOW_H
#define NOTEPADWINDOW_H

#include <QMainWindow>

class NotepadWindow : public QMainWindow {
    Q_OBJECT
    
public:
    NotepadWindow(QWidget *parent = 0);
    ~NotepadWindow();
};

#endif // NOTEPADWINDOW_H
