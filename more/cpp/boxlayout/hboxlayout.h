#ifndef HBOXLAYOUT_H
#define HBOXLAYOUT_H

#include "boxlayout.h"

class HBoxLayout : public BoxLayout
{
public:
    HBoxLayout();
    Box containing_box();
};

#endif // HBOXLAYOUT_H
