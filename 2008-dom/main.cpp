/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2008
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>

#include "node.h"
#include "element.h"
#include "text.h"

using namespace std;

int main(int argc, char *argv[])
{
    Element* title = new Element("title");
    title->addNode(new Text("The document title"));

    Element* head = new Element("head");
    head->addNode(title);

    Element* body = new Element("body");
    body->addNode(new Text("The document content"));
    body->addAttribute("id", "123");
    body->addAttribute("lang", "it");

    Element* html = new Element("html");
    html->addNode(head);
    html->addNode(body);

    html->print(cout, 0);
    delete html;
    return 0;
}
