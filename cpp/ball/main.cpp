#include "ball.hpp"
#include <iostream>

using std::cout;
using std::endl;

int main() {
    Ball ball1{40, 80};
    auto ball2 = new Ball{80, 40};


    for (auto i = 0; i < 25; ++i) {
        ball1.move();
        ball2->move();

        cout << ball1.get_x() << ", " << ball1.get_y() << endl;
        cout << ball2->get_x() << ", " << ball2->get_y() << endl << endl;
    }

    delete ball2;
    return 0;
}

