/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2008
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "pair.h"

using namespace std;

Pair::Pair(string key, string value)
{
    this->key = key;
    this->value = value;
}

string Pair::getKey()
{
    return key;
}

string Pair::getValue()
{
    return value;
}
