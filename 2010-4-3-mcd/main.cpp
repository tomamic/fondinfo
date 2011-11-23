#include <iostream>

using namespace std;

int mcd(int m, int n) {
    if (m > n) {
        int tmp = m;
        m = n;
        n = tmp;
    }

    cout << "mcd(" << m << ", " << n << ")" << endl;

    return (m == 0) ? n : mcd(m, n % m);
}

int mcd2(int m, int n) {
    do {
        if (m > n) {
            int tmp = m;
            m = n;
            n = tmp;
        }

        cout << "mcd2(" << m << ", " << n << ")" << endl;

        if (m != 0) {
            n = n % m;
        }
    } while (m > 0);
    return n;
}

int main(int argc, char *argv[])
{
    int m = 72, n = 96;
    cin >> m >> n;
    cout << mcd(m, n) << endl;
    cout << mcd2(m, n) << endl;

    return 0;
}
