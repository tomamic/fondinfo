/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2008
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef NODE_H
#define NODE_H

#include <iostream>

using namespace std;

class Node
{
public:
    Node();
    virtual ~Node();
    virtual void print(ostream &out, int indent) = 0;
};

#endif // NODE_H
