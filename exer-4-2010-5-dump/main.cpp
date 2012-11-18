/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[]) {
    const int LENGTH = 16;

    string fileName;
    if (argc > 1) {
        fileName = argv[1];
    } else {
        cout << "Insert the file name: " << endl;
        cin >> fileName;
    }

    ifstream file(fileName.c_str(), ios::binary);

    while (file.good()) {
        string line;
        for (int i = 0; i < LENGTH; ++i) {
            char c = file.get();
            if (file.good()) {
                cout << setfill('0') << setw(2) << hex
                     << int(c) << ' ';
                if (' ' <= c && c <= '~') line += c;
                else line += ' ';
            } else {
                cout << "   ";
            }
        }
        cout << '\t' << line << endl;
        line = "";
    }

    file.close();
    return 0;
}
