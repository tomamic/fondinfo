/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

using namespace std;

/* Proof. Since n is composite, n = d*e for some natural numbers
   d and e which are not zero and not units. If both of them are
   greater than sqrt(n), then n = d*e > sqrt(n)*sqrt(n) = n, so
   n>n, contradiction. So d or e is <= sqrt(n). */

int main(int argc, char *argv[])
{
    int n, d = 2;
    cin >> n;

    // for (d = 2; d < n/2 && n%d != 0; ++d) { }
	
    if (n % d != 0) {
        for (d = 3; d*d <= n && n%d != 0; d += 2) { }
    }

    if (n % d == 0 && n != d) {
        cout << "The number is divisible by " << d << endl;
    } else {
        cout << "The number is prime" << endl;
    }

    return 0;
}
