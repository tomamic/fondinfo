/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
