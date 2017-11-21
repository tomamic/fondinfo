#include "hboxlayout.h"

HBoxLayout::HBoxLayout() {
}

Box HBoxLayout::containing_box() {
    int width = 0, height = 0;
    for (auto box : boxes_) {
        width += box->width();
        if (box->height() > height) {
            height = box->height();
        }
    }
    return Box{width, height};
}
