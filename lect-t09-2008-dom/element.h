/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
