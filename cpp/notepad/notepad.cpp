#include "notepad.h"

#include <fstream>

#include <QFileDialog>
#include <QMessageBox>
#include <QHBoxLayout>
#include <QVBoxLayout>

using namespace std;

Notepad::Notepad() {
    // ctor: build the GUI
    // QObject::tr translates GUI texts (see Qt Linguist)

    auto button_layout = new QVBoxLayout;
    button_layout->addWidget(open_button);
    button_layout->addWidget(save_button);
    button_layout->addWidget(exit_button);
    button_layout->addStretch();

    auto main_layout = new QHBoxLayout;
    main_layout->addWidget(text_edit);
    main_layout->addLayout(button_layout);
    setLayout(main_layout);

    connect(open_button, &QPushButton::clicked, this, &Notepad::open);
    connect(save_button, &QPushButton::clicked, this, &Notepad::save);
    connect(exit_button, &QPushButton::clicked, this, &Notepad::exit);
}

Notepad::~Notepad() {
}

void Notepad::open() {
    // choose the input file
    auto filename = QFileDialog::getOpenFileName(this).toStdString();
    if (filename != "") {
        ifstream fin{filename};
        if (fin) {
            // read the whole text
            string content; getline(fin, content, '\0');
            text_edit->setText(content.c_str());
        } else {
            QMessageBox::critical(this, tr("Error"),
                                  tr("Could not open file"));
        }
    }
}

void Notepad::save() {
    // choose the output file
    auto filename = QFileDialog::getSaveFileName(this).toStdString();
    if (filename != "") {
        ofstream fout{filename};
        if (fout) {
            // write the whole text
            auto text = text_edit->toPlainText().toStdString();
            fout << text;
        } else {
            QMessageBox::critical(this, tr("Error"),
                                  tr("Could not save file"));
        }
    }
}

void Notepad::exit() {
    auto button = QMessageBox::question(
                this,
                tr("Notepad - Quit"),
                tr("Do you really want to quit?"),
                QMessageBox::Yes | QMessageBox::No);

    if (button == QMessageBox::Yes) {
        window()->close();
    }
}
