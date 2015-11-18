#include "notepadwindow.h"
#include "notepad.h"

#include <QAction>
#include <QMenu>
#include <QMenuBar>
#include <QToolBar>
#include <QStyle>

NotepadWindow::NotepadWindow() {
    auto notepad = new Notepad; setCentralWidget(notepad);

    auto menu = menuBar()->addMenu(tr("&File"));  // QMenu*
    auto open_act = menu->addAction(tr("&Open"));  // QAction*
    auto save_act = menu->addAction(tr("&Save"));
    menu->addSeparator();
    auto exit_act = menu->addAction(tr("E&xit"));

    open_act->setIcon(style()->standardIcon(QStyle::SP_DialogOpenButton));
    save_act->setIcon(style()->standardIcon(QStyle::SP_DialogSaveButton));
    exit_act->setIcon(style()->standardIcon(QStyle::SP_DialogCloseButton));

    auto tools = addToolBar(tr("&File"));  // QToolBar*
    tools->addAction(open_act);
    tools->addAction(save_act);
    tools->addSeparator();
    tools->addAction(exit_act);

    connect(open_act, &QAction::triggered, notepad, &Notepad::open);
    connect(save_act, &QAction::triggered, notepad, &Notepad::save);
    connect(exit_act, &QAction::triggered, notepad, &Notepad::exit);
}

NotepadWindow::~NotepadWindow() {
}
