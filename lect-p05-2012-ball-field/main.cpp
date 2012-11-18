/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include "field.h"
#include "ball.h"

using namespace std;

int main()
{

    ofstream out("game.txt");

    const int WIDTH = 16;
    const int HEIGHT = 12;
    Field* field = new Field(WIDTH, HEIGHT);
    field->add(new Ball(4, 8, +1, +1, WIDTH, HEIGHT));
    field->add(new Ball(12, 4, +1, +1, WIDTH, HEIGHT));
    field->add(new Ball(8, 6, +1, +1, WIDTH, HEIGHT));
    field->print(cout);

    string line;
    while (getline(cin, line)) {
        field->moveAll();
        field->print(cout);
    }

    field->print(out);

    delete field;
    return 0;
}

