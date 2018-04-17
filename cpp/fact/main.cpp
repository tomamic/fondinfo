#include <iostream>

using namespace std;

int fact_tr(int n, int acc) {
    if (n == 0) return acc;
    return fact_tr(n - 1, acc * n);
}

int main()
{
    cout << fact_tr(4, 1) << endl;
    return 0;
}
