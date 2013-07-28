/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "notepad.h"

#include <QtGui/QApplication>
#include <QtGui/QMainWindow>
#include <QtGui/QAction>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QToolBar>
#include <QtGui/QFileDialog>
#include <QtGui/QMessageBox>
#include <fstream>

using namespace std;

Notepad::Notepad(QWidget* parent) : QMainWindow(parent)
{
    textEdit = new QTextEdit();

    setCentralWidget(textEdit);

    // Create some actions
    QAction* openAction = new QAction(tr("&Open"), this);
    QAction* saveAction = new QAction(tr("&Save"), this);
    QAction* exitAction = new QAction(tr("E&xit"), this);
    connect(openAction, SIGNAL(triggered()), this, SLOT(open()));
    connect(saveAction, SIGNAL(triggered()), this, SLOT(save()));
    connect(exitAction, SIGNAL(triggered()), this, SLOT(exit()));

    // Add all the actions to a menu
    QMenu* fileMenu = menuBar()->addMenu(tr("&File"));
    fileMenu->addAction(openAction);
    fileMenu->addAction(saveAction);
    fileMenu->addSeparator();
    fileMenu->addAction(exitAction);

    // Add all the actions to a toolbar
    QToolBar* toolBar = addToolBar(tr("&File"));
    toolBar->addAction(openAction);
    toolBar->addAction(saveAction);
    toolBar->addSeparator();
    toolBar->addAction(exitAction);

    setWindowTitle(tr("Notepad"));
    show();
}

Notepad::~Notepad()
{
    /* intentionally empty */
}

void Notepad::open()
{
    QString fileName = QFileDialog::getOpenFileName(
                this, tr("Notepad - Open File"));
    if (fileName != "") {
        ifstream file(fileName.toStdString().c_str());
        if (file.good()) {
            // read application data from file stream
            string content;
            getline(file, content, '\0');
            textEdit->setText(content.c_str());
        } else {
            QMessageBox::critical(this, tr("Notepad - Error"),
                                  tr("Could not open file"));
        }
    }
}

void Notepad::save()
{
    QString fileName = QFileDialog::getSaveFileName(
                this, tr("Notepad - Save File"));
    if (fileName != "") {
        ofstream file(fileName.toStdString().c_str());
        if (file.good()) {
            // write application data to file stream
            QString text = textEdit->toPlainText();
            file << text.toStdString();
        } else {
            QMessageBox::critical(this, tr("Notepad - Error"),
                                  tr("Could not save file"));
        }
    }
}

void Notepad::exit()
{
    int button = QMessageBox::question(
                this, tr("Notepad - Quit"),
                tr("Do you really want to quit?"),
                QMessageBox::Yes | QMessageBox::No);

    if (button == QMessageBox::Yes) {
        qApp->quit();
    }
}
