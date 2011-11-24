/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2008
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
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
