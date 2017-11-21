/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
    const char FIRST = 'A';

    srand(time(NULL));

    int rows = 1, cols = 1, size = 1;
    while (size % 2 != 0) {
        cout << "Rows and cols?" << endl;
        cin >> rows >> cols;
        size = rows * cols;
    }

    vector<char> matrix(size);
    for (int i = 0; i < size; ++i) {
        matrix[i] = FIRST + i/2;
    }

    for (int i = 0; i < size; ++i) {
        cout << matrix[i];
        if (i % cols == cols - 1) cout << endl;
    }
    cout << endl;

    for (int i = 0; i < size; ++i) {
        int j = rand() % size;
        int temp = matrix[i];
        matrix[i] = matrix[j];
        matrix[j] = temp;
    }

    for (int i = 0; i < size; ++i) {
        cout << matrix[i];
        if (i % cols == cols - 1) cout << endl;
    }

    return 0;
}
