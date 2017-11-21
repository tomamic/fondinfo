#ifndef VBOXLAYOUT_H
#define VBOXLAYOUT_H

#include "boxlayout.h"

class VBoxLayout : public BoxLayout
{
public:
    VBoxLayout();
    Box containing_box();
};

#endif // VBOXLAYOUT_H
