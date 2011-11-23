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
