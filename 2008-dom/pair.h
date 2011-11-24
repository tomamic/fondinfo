/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2008
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
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
