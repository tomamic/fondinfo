#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    const string END = "end";
    int count = 0;
    int length = 0;

    string word;
    cin >> word;
    while (word != END) {
        ++count;
        length += word.size();
        cin >> word;
    }

    if (count != 0) {
        cout << (length / count) << endl;
    }

    return 0;
}
