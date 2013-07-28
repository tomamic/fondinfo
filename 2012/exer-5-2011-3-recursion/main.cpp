/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <cmath>

using namespace std;

float sqrtRecursion(float x, float low, float high)
{
    float y = (high + low) / 2;
    float delta = y * y - x;

    if (delta < -0.001 || 0.001 < delta) {
        if (delta < 0) {
           y = sqrtRecursion(x, y, high);
        } else {
            y = sqrtRecursion(x, low, y);
        }
    }

    return y;
}

int main(int argc, char *argv[])
{
    float x;
    cin >> x;

    float low = 0;
    float high = x;
    if (high < 1) high = 1;

    cout << sqrtRecursion(x, low, high) << endl;
    cout << sqrt(x) << endl;
    return 0;
}
