/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
