/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "element.h"

using namespace std;

Element::Element(string type)
{
    this->type = type;
}

Element::~Element()
{
    while (children.size() > 0) {
        delete children.back();
        children.pop_back();
    }
    while (attributes.size() > 0) {
        delete attributes.back();
        attributes.pop_back();
    }
}

void Element::addNode(Node* node)
{
    children.push_back(node);
}

void Element::addAttribute(string key, string value)
{
    attributes.push_back(new Pair(key, value));
//    attributes[key] = value;
}

void Element::print(ostream &out, int indent)
{
    string leadingSpaces(indent, ' ');
    out << leadingSpaces << "<" << type;
    printAttributes(out);
    out << ">" << endl;
    printChildren(out, indent);
    out << leadingSpaces << "</" << type << ">" << endl;
}

void Element::printChildren(ostream &out, int indent)
{
    for (int i = 0; i < children.size(); ++i) {
        children[i]->print(out, indent + 2);
    }
}

void Element::printAttributes(ostream &out)
{
    for (int i = 0; i < attributes.size(); ++i) {
        Pair* p = attributes[i];
        out << ' ' << p->getKey();
        out << "=\"" << p->getValue() << "\"";
    }

//    map<string, string>::iterator i;
//    for (i = attributes.begin(); i != attributes.end(); ++i) {
//        out << ' ' << i->first << "=\"" << i->second << "\"";
//    }
}
