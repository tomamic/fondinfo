/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <cmath>

using namespace std;

float sqrtBisection(float x)
{
    float low = 0;
    float high = x;
    if (high < 1) high = 1;
    float y = (high + low) / 2;
    float delta = y * y - x;

    while (delta < -0.001 || 0.001 < delta) {
        if (delta < 0) {
           low = y;
        } else {
            high = y;
        }
        y = (high + low) / 2;
        delta = y * y - x;
    }
    return y;
}

int main(int argc, char *argv[])
{
    float x;
    cin >> x;
    cout << sqrtBisection(x) << endl;
    cout << sqrt(x) << endl;
    return 0;
}
