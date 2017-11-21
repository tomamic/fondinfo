#ifndef BOXLAYOUT_H
#define BOXLAYOUT_H

#include "box.h"
#include <vector>

using namespace std;

class BoxLayout
{
public:
    BoxLayout();
    void add(Box* box);
    int sum_areas();
    virtual Box containing_box() = 0;
protected:
    vector<Box*> boxes_;
};

#endif // BOXLAYOUT_H
