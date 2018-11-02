#include <iostream>
#include "actor.h"
#include "bounce.h"

using namespace std;

int main()
{
    auto arena = new Arena{320, 240};
    new Ball{arena, 40, 80};
    new Ball{arena, 80, 40};
    new Ghost{arena, 120, 80};
    auto turtle = new Turtle{arena, 80, 80};

    for (string line; getline(cin, line);) {
        if (line == "w") turtle->go_up();
        else if (line == "a") turtle->go_left();
        else if (line == "s") turtle->go_down();
        else if (line == "d") turtle->go_right();
        else if (line == " ") turtle->stay();

        arena->move_all();
        for (auto a : arena->actors()) {
            auto pos = a->position();
            cout << pos[0] << " " << pos[1] << endl;
        }
        cout << endl;
    }
    return 0;
}

