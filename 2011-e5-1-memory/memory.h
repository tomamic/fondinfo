/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef MEMORY_H
#define MEMORY_H

#include <vector>
#include <iostream>

using namespace std;

class Memory
{
public:
    Memory(int rows, int cols);
    void init();
    void shuffle();
    void move(int card1, int card2);
    bool isSolved();
    void write(ostream& out);

    static const char JOLLY = '?';
    static const char FIRST = 'A';
    static const char LAST = 'Z';
    static const char FIRST_HIDDEN = 'a';
    static const char LAST_HIDDEN = 'z';

private:
    vector<char> matrix;
    int cols;
    int rows;
    int move1;
    int move2;
};

#endif // MEMORY_H
