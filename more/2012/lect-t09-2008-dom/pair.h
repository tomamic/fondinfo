/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef PAIR_H
#define PAIR_H

#include <string>

using namespace std;

class Pair
{
public:
    Pair(string key, string value);
    string getKey();
    string getValue();

private:
    string key;
    string value;
};

#endif // PAIR_H
