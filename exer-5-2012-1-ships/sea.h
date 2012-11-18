/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef SEA_H
#define SEA_H

#include <iostream>
#include <vector>

using namespace std;

class Sea
{
public:
    Sea(int rows, int cols);
    bool place(int y, int x, int dir, int size);
    void print(ostream& out);
    int getRows();
    int getCols();
    int getDirs();
private:
    int rows;
    int cols;
    vector< vector<bool> > matrix;
};

#endif // SEA_H
