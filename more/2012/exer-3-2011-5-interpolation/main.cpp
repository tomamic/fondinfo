/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in("../2011-3-5-interpolation/sin.txt");
    vector<float> function;

    float val;
    in >> val;
    while (in.good()) {
        function.push_back(val);
        in >> val; // val = sin(i * 2 * M_PI / 360);
    }
    int period = function.size();

    float angle;
    cout << "Angle?" << endl;
    cin >> angle;
    while (cin.good()) {
        int x1 = int(angle); // int close to zero
        if (angle < x1) --x1; // needed for negative, non-integer values
        // int x1 = floor(angle);
        float fract = angle - x1;

        x1 = x1 % period; // traslate into the base range, considering periodicity
        if (x1 < 0) x1 += period; // consider negative remainder; dividend = quotient * divisor + remainder
        int x2 = (x1 + 1) % period; // x2 is the next integer, in the base range
        //clog << angle << ": x1=" << x1 << " x2=" << x2 << " fract=" << fract << endl;

        float y1 = function[x1];
        float y2 = function[x2];
        cout << (y1 + fract * (y2 - y1)) << endl;

        cout << "Angle?" << endl;
        cin >> angle;
    }
}
