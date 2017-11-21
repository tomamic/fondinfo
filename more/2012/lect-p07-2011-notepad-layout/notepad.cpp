/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "notepad.h"

#include <QtGui/QApplication>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QFileDialog>
#include <QtGui/QMessageBox>
#include <fstream>

using namespace std;

Notepad::Notepad(QWidget* parent) : QWidget(parent)
{
    textEdit = new QTextEdit();

    QPushButton* openButton = new QPushButton(tr("&Open"), this);
    QPushButton* saveButton = new QPushButton(tr("&Save"), this);
    QPushButton* exitButton = new QPushButton(tr("E&xit"), this);

    QVBoxLayout* vLayout = new QVBoxLayout();
    vLayout->addWidget(openButton);
    vLayout->addWidget(saveButton);
    vLayout->addWidget(exitButton);
    vLayout->addStretch();

    QHBoxLayout* hLayout = new QHBoxLayout();
    hLayout->addWidget(textEdit);
    hLayout->addLayout(vLayout);

    setLayout(hLayout);

    //    setCentralWidget(new QWidget()); // if derived from QMainWindow
    //    centralWidget()->setLayout(hLayout);

    connect(openButton, SIGNAL(clicked()), this, SLOT(open()));
    connect(saveButton, SIGNAL(clicked()), this, SLOT(save()));
    connect(exitButton, SIGNAL(clicked()), this, SLOT(exit()));

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
        ifstream in(fileName.toStdString().c_str()); // c++03
        if (in.good()) {
            // read application data from file stream
            string content;
            getline(in, content, '\0');
            textEdit->setText(content.c_str());
        } else {
            QMessageBox::critical(this, tr("Notepad - Error"),
                                  tr("Could not open file"));
        }
    }
}


void Notepad::save() {
    QString fileName = QFileDialog::getSaveFileName(
                this, tr("Notepad - Save File"));
    if (fileName != "") {
        ofstream out(fileName.toStdString().c_str());
        if (out.good()) {
            // write application data to file stream
            QString text = textEdit->toPlainText();
            out << text.toStdString();
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
