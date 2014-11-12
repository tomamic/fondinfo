#include "file.h"

using namespace std;

File::File(string name, string text)
{
    this->name = name;
    this->text = text;
}

int File::size()
{
    return text.size();
}

void File::print(int indent)
{
    for (auto i = 0; i < indent; ++i) cout << ' ';
    cout << name << endl;
}
