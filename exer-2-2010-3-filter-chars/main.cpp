/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {

    string text;
    getline(cin, text);

    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];

        if (c < '0' || c > '9') {
            cout << c;
        }
    }
    cout << endl;

    return 0;
}
