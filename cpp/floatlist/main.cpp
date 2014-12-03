#include <iostream>
#include <cassert>
#include "floatvector.h"
#include "floatlist.h"
#include "genericlist.h"

using namespace std;

int main() {

    // test vector

    FloatVector u{3, 10};
    assert(u.str() == "10 10 10");

    FloatVector v;
    assert(v.str() == "");

    for (int i = 0; i  < 6; ++i) v.push(0);
    assert(v.str() == "0 0 0 0 0 0");

    for (int i = 0; i  < v.size(); ++i) v.set(i, float(i));
    assert(v.get(2) == 2);
    assert(v.str() == "0 1 2 3 4 5");

    v.remove(1);
    v.insert(3, 10);
    assert(v.str() == "0 2 3 10 4 5");

    v.insert(0, 11);
    assert(v.str() == "11 0 2 3 10 4 5");

    v.remove(0);
    assert(v.str() == "0 2 3 10 4 5");

    int v_back = v.pop();
    assert(v_back == 5);
    assert(v.str() == "0 2 3 10 4");

    v.push(11);
    assert(v.str() == "0 2 3 10 4 11");

    // test list

    FloatList k{3, 10};
    assert(k.str() == "10 10 10");

    FloatList l;
    assert(l.str() == "");

    for (int i = 0; i  < 6; ++i) l.push(0);
    assert(l.str() == "0 0 0 0 0 0");

    for (int i = 0; i  < l.size(); ++i) l.set(i, float(i));
    assert(l.get(2) == 2);
    assert(l.str() == "0 1 2 3 4 5");

    l.remove(1);
    l.insert(3, 10);
    assert(l.str() == "0 2 3 10 4 5");

    l.insert(0, 11);
    assert(l.str() == "11 0 2 3 10 4 5");

    l.remove(0);
    assert(l.str() == "0 2 3 10 4 5");

    int l_back = l.pop();
    assert(l_back == 5);
    assert(l.str() == "0 2 3 10 4");

    l.push(11);
    assert(l.str() == "0 2 3 10 4 11");

    GenericList<int> m{3, 10};
    assert(m.str() == "10 10 10");

    return 0;
}
