#include "box.h"

Box::Box(int width, int height) {
    width_ = width;
    height_ = height;
}

int Box::width() const {
    return width_;
}

int Box::height() const {
    return height_;
}

int Box::area() const {
    return width_ * height_;
}

int Box::perimeter() const {
    return 2 * (width_ + height_);
}
