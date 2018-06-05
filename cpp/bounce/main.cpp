#include <iostream>
#include "actor.h"
#include "bounce.h"

using namespace std;

int main()
{
    auto arena = new Arena{320, 240};
    auto ball1 = new Ball{arena, 40, 80};
    auto ball2 = new Ball{arena, 80, 40};
    auto ghost = new Ghost{arena, 120, 80};
    auto turtle = new Turtle{arena, 80, 80};

    string line;
    while (getline(cin, line)) {
        if (line == "w") turtle->go_up();
        else if (line == "a") turtle->go_left();
        else if (line == "s") turtle->go_down();
        else if (line == "d") turtle->go_right();

        arena->move_all();
        for (auto a : arena->actors()) {
            auto pos = a->position();
            cout << pos[0] << " " << pos[1] << endl;
        }
        cout << endl;
    }
    return 0;
}

