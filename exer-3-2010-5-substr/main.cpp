/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    string text = "Scrivete a <john@example.com> o <tom@example.com> per informazioni";
    string match = "";
    bool inside = false;

    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];
        if (c == '<') {
            match = "";
            inside = true;
        } else if (c == '>' && inside) {
            cout << match << endl;
            match = "";
            inside = false;
        } else if (inside) {
            match += c;
        }
    }

    return 0;
}
