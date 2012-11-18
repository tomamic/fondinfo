/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef FLOWERSPUZZLE_H
#define FLOWERSPUZZLE_H

#include <vector>
#include <iostream>

using namespace std;

class FlowersPuzzle
{
public:
    FlowersPuzzle(int height, int width, int flowers);
    void shuffle();

    int getRows();
    int getColumns();
    char getMap(int y, int x);
    char getView(int y, int x);

    void uncover(int y, int x);
    void flag(int y, int x);

    bool isWon();
    bool isLost();

    void write(ostream& out);

    static const char FLOWER = '*';
    static const char UNKNOWN = '.';
    static const char FLAG = 'F';
    static const char ZERO = '0';
    static const char OUT_OF_BOUNDS = '!';

private:
    int rows;
    int columns;
    int flowers;
    vector< vector<char> > map;
    vector< vector<char> > view;
    int uncovered;
    int flagged;
    int lastY;
    int lastX;

    void setMap(int y, int x, int val);
    void setView(int y, int x, int val);
    int countFlowers(int y, int x);
    void uncoverAround(int y, int x);
};

#endif // FLOWERSPUZZLE_H
