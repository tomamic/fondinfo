#include <iostream>

using namespace std;

const char PLAYER = 'B';
const char OPPONENT = 'W';

bool check(string& line, int pos, char val)
{
    return (0 <= pos && pos < line.size() && line[pos] == val);
}

int capture(string& line, int pos, int dir)
{
    int i = pos, count = 0;
    while (check(line, i, OPPONENT)) {
        ++count;
        i += dir;
    }
    if (count > 0 && check(line, i, PLAYER)) {
        i = pos;
        while (check(line, i, OPPONENT)) {
            line[i] = PLAYER;
            i += dir;
        }
    } else {
        count = 0;
    }
    return count;
}

int main()
{
    string line; // es. "-BWW-WWB-"
    int pos; // es. 4
    while (cin >> line >> pos) {
        int count = 0;
        count += capture(line, pos + 1, +1);
        count += capture(line, pos - 1, -1);
        if (count > 0) {
            line[pos] = PLAYER;
        }
        cout << line << endl;
    }
    return 0;
}
