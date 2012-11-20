/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

const char PLAYER = 'B';
const char OPPONENT = 'W';
const char EMPTY = '-';

bool check(string& line, int pos, char val)
{
    return (0 <= pos && pos < line.size() && line[pos] == val);
}

int capture(string& line, int pos, int dir)
{
    int i = pos + dir, count = 0;
    while (check(line, i, OPPONENT)) {
        ++count;
        i += dir;
    }
    if (count > 0 && check(line, i, PLAYER)) {
        i = pos + dir;
        while (check(line, i, OPPONENT)) {
            line[i] = PLAYER;
            i += dir;
        }
    } else {
        count = 0;
    }
    return count;
}

void play(string& line, int pos)
{
    if (check(line, pos, EMPTY)) {
        int count = 0;
        count += capture(line, pos, +1);
        count += capture(line, pos, -1);
        if (count > 0) {
            line[pos] = PLAYER;
        }
    }
}

int main()
{
    string line; // es. "-BWW-WWB-"
    int pos; // es. 4
    while (cin >> line >> pos) {
        play(line, pos);
        cout << line << endl;
    }
    return 0;
}

