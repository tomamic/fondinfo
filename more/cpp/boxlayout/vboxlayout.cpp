#include "vboxlayout.h"

VBoxLayout::VBoxLayout() {
}

Box VBoxLayout::containing_box() {
    int width = 0, height = 0;
    for (auto box : boxes_) {
        height += box->height();
        if (box->width() > width) {
            width = box->width();
        }
    }
    return Box{width, height};
}
