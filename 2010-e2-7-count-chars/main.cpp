/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
    string text =
            "Il C++ e` un linguaggio di programmazione orientato agli "
            "oggetti, con tipizzazione statica. E` stato sviluppato (in "
            "origine col nome di 'C con classi') da Bjarne Stroustrup ai "
            "Bell Labs nel 1983 come un miglioramento del linguaggio C. "
            "Tra i miglioramenti principali troviamo: l'introduzione del "
            "paradigma di programmazione a oggetti (le classi), funzioni "
            "virtuali, overloading degli operatori, ereditarieta` multipla, "
            "template e gestione delle eccezioni.";
    string chars;
    cin >> chars;

    int count = 0;
    for (int i = 0; i < text.size(); ++i) {
        char c = text[i];

        bool found = false;
        for (int j = 0; j < chars.size() && !found; ++j) {
            if (c == chars[j]) {
                found = true;
                ++count;
            }
        }
    }
    cout << count;

    return 0;
}
