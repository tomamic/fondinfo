/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2008
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef ELEMENT_H
#define ELEMENT_H

#include "node.h"
#include "pair.h"

#include <string>
#include <vector>
#include <map>

using namespace std;

class Element : public Node
{
public:
    Element(string type);
    ~Element();
    void addNode(Node* node);
    void addAttribute(string key, string value);
    void print(ostream &out, int indent);

private:
    void printAttributes(ostream &out);
    void printChildren(ostream &out, int indent);
    string type;
    vector<Node*> children;
    vector<Pair*> attributes;
//    map<string, string> attributes;
};

#endif // ELEMENT_H
