/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef AKARIPUZZLE_H
#define AKARIPUZZLE_H

#include <iostream>
#include <vector>

using namespace std;

class AkariPuzzle
{
public:
    AkariPuzzle();


    void read(istream& in);
    void write(ostream& out);
    void putBulb(int y, int x);

    char get(int y, int x);

    static const char OUT_OF_BOUNDS = '!';
    static const char EMPTY = '.';
    static const char BULB  = '@';
    static const char LIGHT = '+';
    static const char WALL0 = '0';
    static const char WALL1 = '1';
    static const char WALL2 = '2';
    static const char WALL3 = '3';
    static const char WALL4 = '4';
    static const char WALL  = '5';

private:
    void set(int y, int x, char val);
    void illuminate(int y, int x, int dy, int dx);
    bool checkConstraint(int y, int x); // WALL0 <= table[y*columns+x] <= WALL4

    int rows;
    int columns;
    vector<char> table;
};

#endif // AKARIPUZZLE_H
