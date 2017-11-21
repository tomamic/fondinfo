#include "boxlayout.h"

BoxLayout::BoxLayout() {
}

void BoxLayout::add(Box* box) {
    boxes_.push_back(box);
}

int BoxLayout::sum_areas() {
    int area = 0;
    for (auto box : boxes_) area += box->area();
    return area;
}
