#include <iostream>
#include <cassert>
#include "floatvector.h"
#include "floatlist.h"

using namespace std;

int main() {

    // test vector

    FloatVector u{3.0, 10.0};
    assert(u.str() == "10.0 10.0 10.0");

    FloatVector v;
    assert(v.str() == "");

    for (int i = 0; i  < 6; ++i) v.push(0.0);
    assert(v.str() == "0.0 0.0 0.0 0.0 0.0 0.0");

    for (int i = 0; i  < v.size(); ++i) v.set(i, float(i));
    assert(v.get(2) == 2.0);
    assert(v.str() == "0.0 1.0 2.0 3.0 4.0 5.0");

    v.remove(1);
    v.insert(3, 10.0);
    assert(v.str() == "0.0 2.0 3.0 10.0 4.0 5.0");

    v.insert(0, 11.0);
    assert(v.str() == "11.0 0.0 2.0 3.0 10.0 4.0 5.0");

    v.remove(0);
    assert(v.str() == "0.0 2.0 3.0 10.0 4.0 5.0");

    int v_back = v.pop();
    assert(v_back == 5.0);
    assert(v.str() == "0.0 2.0 3.0 10.0 4.0");

    v.push(11.0);
    assert(v.str() == "0.0 2.0 3.0 10.0 4.0 11.0");

    // test list

    FloatList k{3, 10.0};
    assert(k.str() == "10.0 10.0 10.0");

    FloatList l;
    assert(l.str() == "");

    for (int i = 0; i  < 6; ++i) l.push(0.0);
    assert(l.str() == "0.0 0.0 0.0 0.0 0.0 0.0");

    for (int i = 0; i  < l.size(); ++i) l.set(i, float(i));
    assert(l.get(2) == 2.0);
    assert(l.str() == "0.0 1.0 2.0 3.0 4.0 5.0");

    l.remove(1);
    l.insert(3, 10.0);
    assert(l.str() == "0.0 2.0 3.0 10.0 4.0 5.0");

    l.insert(0, 11.0);
    assert(l.str() == "11.0 0.0 2.0 3.0 10.0 4.0 5.0");

    l.remove(0);
    assert(l.str() == "0.0 2.0 3.0 10.0 4.0 5.0");

    int l_back = l.pop();
    assert(l_back == 5.0);
    assert(l.str() == "0.0 2.0 3.0 10.0 4.0");

    l.push(11.0);
    assert(l.str() == "0.0 2.0 3.0 10.0 4.0 11.0");

    return 0;
}
