/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Node {
public:
    virtual ~Node() {}
    virtual int size() = 0;
    virtual void print(int indent) = 0;
};


class Document : public Node {
public:
    Document(string name, string text) {
        this->name = name;
        this->text = text;
    }

    int size() {
        return text.size();
    }

    void print(int indent) {
        for (auto i = 0; i < indent; ++i) cout << ' ';
        cout << name << endl;
    }

private:
    string name;
    string text;
};


class Folder : public Node
{
public:
    Folder(string name) {
        this->name = name;
    }

    ~Folder() {
        clear();
    }

    void clear() {
        while (subnodes.size() > 0) {
            delete_node(subnodes.size() - 1);
        }
    }

    int size() {
        auto total_size = 0;
        for (auto n : subnodes) {
            total_size += n->size();
        }
        return total_size;
    }

    void print(int indent) {
        for (auto i = 0; i < indent; ++i) cout << ' ';
        cout << name << endl;
        for (auto n : subnodes) {
            n->print(indent + 4);
        }
    }

    void add_node(Node* n) {
        subnodes.push_back(n);
    }

    void delete_node(int index) {
        if (0 <= index && index < subnodes.size()) {
            // 1. delete the node object from memory
            // 2. remove its pointer from the vector
            delete subnodes[index];
            subnodes.erase(begin(subnodes) + index);
        }
    }

private:
    string name;
    vector<Node*> subnodes;
};


int main() {
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
