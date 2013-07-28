#include "notepad.h"

#include <fstream>

#include <QFileDialog>
#include <QMessageBox>
#include <QHBoxLayout>
#include <QVBoxLayout>

using namespace std;

Notepad::Notepad(QWidget *parent)
    : QWidget(parent)
{
    // ctor: build the GUI
    // QObject::tr translates GUI texts (see Qt Linguist)

    textEdit = new QTextEdit;
    openButton = new QPushButton{tr("Open")};
    saveButton = new QPushButton{tr("Save")};
    exitButton = new QPushButton{tr("Quit")};

    QVBoxLayout* buttonLayout = new QVBoxLayout;
    buttonLayout->addWidget(openButton);
    buttonLayout->addWidget(saveButton);
    buttonLayout->addWidget(exitButton);
    buttonLayout->addStretch();

    QHBoxLayout* mainLayout = new QHBoxLayout;
    mainLayout->addWidget(textEdit);
    mainLayout->addLayout(buttonLayout);
    setLayout(mainLayout);

    connect(openButton, &QPushButton::clicked, this, &Notepad::open);
    connect(saveButton, &QPushButton::clicked, this, &Notepad::save);
    connect(exitButton, &QPushButton::clicked, this, &Notepad::exit);
}

Notepad::~Notepad()
{
    
}

void Notepad::open() {
    // choose the input file
    QString fileName = QFileDialog::getOpenFileName(this);
    if (fileName != "") {
        ifstream in{fileName.toStdString()};
        if (in.good()) {
            // read the whole text
            string content; getline(in, content, '\0');
            textEdit->setText(content.c_str());
        } else {
            QMessageBox::critical(this, tr("Error"),
                                  tr("Could not open file"));
        }
    }
}

void Notepad::save() {
    // choose the output file
    QString fileName = QFileDialog::getSaveFileName(this);
    if (fileName != "") {
        ofstream out{fileName.toStdString()};
        if (out.good()) {
            // write the whole text
            QString text = textEdit->toPlainText();
            out << text.toStdString();
        } else {
            QMessageBox::critical(this, tr("Error"),
                                  tr("Could not save file"));
        }
    }
}

void Notepad::exit() {
    int button = QMessageBox::question(
                this,
                tr("Notepad - Quit"),
                tr("Do you really want to quit?"),
                QMessageBox::Yes | QMessageBox::No);

    if (button == QMessageBox::Yes) {
        window()->close();
    }
}
