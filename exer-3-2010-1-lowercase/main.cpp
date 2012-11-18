/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    string text = "Hey!! It's 2010, yet";

    bool dash = false;
    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];
        if ('A' <= c && c <= 'Z') {
            c += 'a' - 'A';
            dash = false;
            cout << c;
        } else if (('0' <= c && c <= '9')
            || ('a' <= c && c <= 'z')) {
            dash = false;
            cout << c;
        } else if (!dash) {
            dash = true;
            cout << '-';
        }
    }
    cout << endl;

    return 0;
}
