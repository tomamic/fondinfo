/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
    void sort();
    void shuffle();
    void uncover(int card1, int card2);
    bool isFinished();
    void write(ostream& out);

    // covered cards are represented in lowercase
    // once guessed, they are substitued by the
    // corresponding uppercase, in matrix
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
