#include "document.h"

using namespace std;

Document::Document(string name, string text)
{
    this->name = name;
    this->text = text;
}

int Document::size()
{
    return text.size();
}

void Document::print(int indent)
{
    for (auto i = 0; i < indent; ++i) cout << ' ';
    cout << name << endl;
}
