
#include <iostream>
using namespace std;

void showVolume(int length, int width = 1, int height = 1);
//Returns the volume of a box. 
//If no height is given, the height is assumed to be 1.
//If neither height nor width are given, both are assumed to be 1.

int main( )
{
    showVolume(4, 6, 2);
    showVolume(4, 6);
    showVolume(4);
 
    return 0;
}

void showVolume(int length, int width, int height)
{
    cout << "Volume of a box with \n" 
         << "Length = " << length << ", Width = " << width << endl
         << "and Height = " << height 
         << " is " << length*width*height << endl;
}
