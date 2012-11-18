/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <vector>

using namespace std;

const int DISCS = 5;
const int POLES = 3;
const int SUM_OF_POLE_IDS = 2 + 1 + 0;

void print(vector< vector<int> > &towers) {
    for (int t = 0; t < POLES; ++t) {
        cout << '|';
        for (int i = 0; i < towers[t].size(); ++i) {
            cout << ' ' << towers[t][i];
        }
        cout << endl;
    }
    cin.get();
}

void move(vector< vector<int> > &towers, int n, int from, int to) {
    // find the teporary pole (for this plan)
    int tmp = SUM_OF_POLE_IDS - from - to;

    // if there are discs above, move n-1 away
    if (n > 1) move(towers, n-1, from, tmp);

    // now move the largest disc (of n) to its dest
    int disk = towers[from].back();
    towers[from].pop_back();
    towers[to].push_back(disk);
    print(towers);

    // if there were discs above, move those on top
    if (n > 1) move(towers, n-1, tmp, to);
}

int main() {
    // 3 empty "towers"
    vector< vector<int> > towers(POLES);
    // put discs, first the large one
    for (int i = DISCS; i > 0; --i) {
        towers[0].push_back(i);
    }
    print(towers);

    // move all discs from pole 0 to pole 2
    move(towers, DISCS, 0, POLES-1);

    return 0;
}
