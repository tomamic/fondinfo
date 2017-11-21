/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <iomanip>

using namespace std;

double f3(double x) {
    return x*x*x-x-1;
}

double findZero(double f(double), double min, double max, double error) {
    double x = (max + min) / 2;
    double y = f(x);
    if (y < -error || error < y) {
        if (y * f(min) < 0) {
            x = findZero(f, min, x, error);
        } else {
            x = findZero(f, x, max, error);
        }
    }
    return x;
}

int main(int argc, char *argv[])
{
    double x = findZero(f3, 1, 2, 1e-6);
    cout << setprecision(6) << x << endl;
    
    return 0;
}
