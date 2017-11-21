/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "text.h"

using namespace std;

Text::Text(string text)
{
    this->text = text;
}

void Text::print(ostream &out, int indent)
{
    string leadingSpaces(indent, ' ');
    out << leadingSpaces << text << endl;
}
