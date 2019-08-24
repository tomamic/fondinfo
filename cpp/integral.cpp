/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>

double f(double x) {
    return x * x + x;
}

double integral(double a, double b, int n) {
    /**
     * Estimate the area beneath the curve f, between the
     * abscissas a and b; the region is approximated as n rectangles.
     */
    auto total = 0.0;
    auto dx = (b - a) / n;
    for (auto i = 0; i < n; ++i) {
        total += dx * f(a + dx * i);
    }
    return total;
}

int main() {
    std::cout << integral(1, 10, 100000000) << std::endl;
}
