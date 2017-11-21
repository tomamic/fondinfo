/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "polygon.h"
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    cout << "Polygon?" << endl;

    Polygon x;
    x.read(cin); // CTRL+D / CTRL+Z to close the cin stream and terminate input

    cout << x.perimeter() << endl;

    ofstream out("../exer-5-2011-5-polygon/polygon.txt");
    x.write(out);

    return 0;
}
