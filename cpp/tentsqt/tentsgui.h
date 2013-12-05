#ifndef TENTSGUI_H
#define TENTSGUI_H

#include <QMainWindow>
#include <QPushButton>
#include "tentspuzzle.h"

class TentsGui : public QMainWindow {
    Q_OBJECT
    
public:
    TentsGui(TentsPuzzle* puzzle);
    ~TentsGui();
private:
    void handle_click(int x, int y);
    void update_button(int x, int y);
    void update_all_buttons();

    std::vector<QPushButton*> buttons_;
    TentsPuzzle* puzzle_;
};

#endif // TENTSGUI_H
