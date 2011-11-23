#include <iostream>
#include "memory.h"
#include <cstdlib>
#include <ctime>

int main(int argc, char *argv[])
{
    srand(time(NULL));

    int rows = 1, cols = 1, size = 1;
    while (size % 2 != 0) {
        cout << "Rows and cols?" << endl;
        cin >> rows >> cols;
        size = rows * cols;
    }

    Memory memory(rows, cols);
    memory.write(cout);

    do {
        int a, b;
        cout << "Two cards (1-" << size << ")?" << endl;
        cin >> a >> b;
        memory.move(a - 1, b - 1);
        memory.write(cout);
    } while (! memory.isSolved());

    return 0;
}
