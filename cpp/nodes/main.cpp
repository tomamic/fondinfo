#include <iostream>

#include "document.h"
#include "folder.h"

using namespace std;

int main()
{
    auto a1_0 = new Document("a1.txt", "bla bla 0");
    auto report = new Document("report.dat", "some reports");
    auto data = new Folder("data");
    data->add_node(report);
    auto cmpt166 = new Folder("cmpt166");
    cmpt166->add_node(a1_0);
    cmpt166->add_node(data);
    auto a1_1 = new Document("a1.txt", "a different file");
    auto macm101 = new Folder("macm101");
    macm101->add_node(a1_1);
    auto desktop = new Folder("Desktop");
    desktop->add_node(cmpt166);
    desktop->add_node(macm101);

    cout << desktop->size() << endl << endl;

    desktop->print(0);

    delete desktop;
    return 0;
}

