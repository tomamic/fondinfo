#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char*argv[]) {

    //ifstream in("../2010-3-3-scytale/main.cpp");
    //istringstream in("Il C++ e` un linguaggio di programmazione orientato agli oggetti, con tipizzazione statica. E` stato sviluppato (in origine col nome di 'C con classi' da Bjarne Stroustrup ai Bell Labs nel 1983 come un miglioramento del linguaggio C. Tra i miglioramenti principali troviamo: l'introduzione del paradigma di programmazione a oggetti (le classi), funzioni virtuali, overloading degli operatori, ereditarieta` multipla, template e gestione delle eccezioni.");

    ifstream in("../2010-3-3-scytale/main.cpp");
    ofstream out("out.txt");
    const int M = 3, N = 4;
    char matrix[M][N]; // M, N should be constants! (standard C++)
    // vector<vector<char> > matrix(M, vector<char>(N));

    while (in.good()) {
        for (int y = 0; y < M; ++y) {
            for (int x = 0; x < N; ++x) {
                char c; in.get(c);
                if (in.good()) {
                    matrix[y][x] = c;
                } else {
                    matrix[y][x] = ' ';
                }
            }
        }

        for (int x =0; x < N; ++x) {
            for (int y = 0; y < M; ++y) {
                out << matrix[y][x];
            }
        }
    }

    return 0;
}
