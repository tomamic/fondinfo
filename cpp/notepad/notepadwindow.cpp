#include "notepadwindow.h"
#include "notepad.h"

#include <QAction>
#include <QMenu>
#include <QMenuBar>
#include <QToolBar>
#include <QStyle>

NotepadWindow::NotepadWindow(QWidget *parent)
    : QMainWindow(parent)
{
    auto notepad = new Notepad; setCentralWidget(notepad);

    auto menu = menuBar()->addMenu(tr("&File"));  // QMenu*
    auto openAct = menu->addAction(tr("&Open"));  // QAction*
    auto saveAct = menu->addAction(tr("&Save"));
    menu->addSeparator();
    auto exitAct = menu->addAction(tr("E&xit"));

    openAct->setIcon(style()->standardIcon(QStyle::SP_DialogOpenButton));
    saveAct->setIcon(style()->standardIcon(QStyle::SP_DialogSaveButton));
    exitAct->setIcon(style()->standardIcon(QStyle::SP_DialogCloseButton));

    auto tools = addToolBar(tr("&File"));  // QToolBar*
    tools->addAction(openAct);
    tools->addAction(saveAct);
    tools->addSeparator();
    tools->addAction(exitAct);

    connect(openAct, &QAction::triggered, notepad, &Notepad::open);
    connect(saveAct, &QAction::triggered, notepad, &Notepad::save);
    connect(exitAct, &QAction::triggered, notepad, &Notepad::exit);
}

NotepadWindow::~NotepadWindow()
{
    
}
