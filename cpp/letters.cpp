/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    vector<int> letters;
    letters.assign(26, 0);

    ifstream fin{"../exercises/cpp.txt"};

    string line;
    if (fin) {
        getline(fin, line, '\0');
    }
    fin.close();

    for (auto c : line) {
        if ('a' <= c && c <= 'z') {
            int index = c - 'a';
            letters[index] += 1;
        }
    }

    ofstream fout{"letters.txt"};
    if (fout) {
        for (auto i = 0; i < letters.size(); ++i) {
            fout << char('a' + i) << ": " << letters[i] << endl;
        }
    }
    fout.close();

    return 0;
}
