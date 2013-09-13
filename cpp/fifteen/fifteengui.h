/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FIFTEENGUI_H
#define FIFTEENGUI_H

#include "fifteenpuzzle.h"

#include <QWidget>
#include <QPushButton>

class FifteenGui : public QWidget
{
    Q_OBJECT

public:
    FifteenGui(FifteenPuzzle* puzzle);

private:
    void fix_appearance();
    void handle_click(int x, int y);
    void update_button(int x, int y);
    void update_all_buttons();

    int cols() { return puzzle_->cols(); }
    int rows() { return puzzle_->rows(); }

    vector<QPushButton*> buttons_;
    FifteenPuzzle* puzzle_;
};

#endif // GAMEGUI_H
