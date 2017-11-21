#include <iostream>
#include "boxlayout.h"
#include "hboxlayout.h"
#include "vboxlayout.h"

using namespace std;

int main() {
    BoxLayout* layout = nullptr;
    cout << "dir (h/v))?" << endl;
    string dir; cin >> dir;
    if (dir == "h") layout = new HBoxLayout{};
    else layout = new VBoxLayout{};

    int width, height;
    cout << "width, height?" << endl;
    cin >> width >> height;
    while (width > 0 && height > 0) {

        Box* box = new Box{width, height};
        layout->add(box);

        cout << "width, height?" << endl;
        cin >> width >> height;
    }

    float used_area = layout->sum_areas();
    Box virtualbox = layout->containing_box();
    float whole_area = virtualbox.area();

    cout << "Used area: " << used_area << endl;
    cout << "Whole area: " << whole_area << endl;
    cout << "Wasted space (ratio): "
         << 1 - (used_area / whole_area) << endl;
}

