/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2008
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef TEXT_H
#define TEXT_H

#include "node.h"

#include <string>

using namespace std;

class Text : public Node
{
public:
    Text(string text);
    void print(ostream &out, int indent);

private:
    string text;
};

#endif // TEXT_H
