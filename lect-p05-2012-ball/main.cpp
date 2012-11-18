/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include "ball.h"

using namespace std;

void print(Ball* ball1, Ball* ball2)
{
    const char BALL1 = 'O';
    const char BALL2 = 'X';
    const char EMPTY = '-';

    for (int y = 0; y < Ball::HEIGHT; ++y) {
        for (int x = 0; x < Ball::WIDTH; ++x) {
            if (x == ball1->getX()
                    && y == ball1->getY()) {
                cout << BALL1;
            } else if (x == ball2->getX()
                       && y == ball2->getY()) {
                cout << BALL2;
            } else {
                cout << EMPTY;
            }
        }
        cout << endl;
    }
    cout << endl;
}

int main()
{
    Ball* ball1 = new Ball(4, 8, +1, +1);
    Ball* ball2 = new Ball(8, 4, +1, +1);
    print(ball1, ball2);

    string line;
    while(getline(cin, line)) {
        ball1->move();
        ball2->move();
        print(ball1, ball2);
    }

    delete ball1;
    delete ball2;
    return 0;
}
