#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream file("../2011-3-1-bracket/main.cpp");
    file >> noskipws;

    bool inside = false;

    char c;
    file >> c;
    while (file.good()) {

        if (c == '(') {
            inside = true;
        } else if (c == ')' && inside) {
            inside = false;
        } else if (!inside) {
            cout << c;
        }

        file >> c;
    }

    return 0;
}
