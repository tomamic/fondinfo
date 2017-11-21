/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
