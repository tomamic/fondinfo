#include "notepadwindow.h"
#include "notepad.h"

#include <QAction>
#include <QMenu>
#include <QMenuBar>
#include <QToolBar>

NotepadWindow::NotepadWindow(QWidget *parent)
    : QMainWindow(parent)
{
    Notepad* notepad = new Notepad; setCentralWidget(notepad);

    QMenu* fileMenu = menuBar()->addMenu(tr("&File"));
    QAction* openAction = fileMenu->addAction(tr("&Open"));
    QAction* saveAction = fileMenu->addAction(tr("&Save"));
    fileMenu->addSeparator();
    QAction* exitAction = fileMenu->addAction(tr("E&xit"));

    connect(openAction, &QAction::triggered, notepad, &Notepad::open);
    connect(saveAction, &QAction::triggered, notepad, &Notepad::save);
    connect(exitAction, &QAction::triggered, notepad, &Notepad::exit);

//    QToolBar* toolBar = addToolBar(tr("&File"));
//    toolBar->addAction(openAction);
//    toolBar->addAction(saveAction);
//    toolBar->addSeparator();
//    toolBar->addAction(exitAction);
}

NotepadWindow::~NotepadWindow()
{
    
}
