/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
