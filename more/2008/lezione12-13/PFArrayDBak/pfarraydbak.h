//This is the header file pfarraydbak.h. This is the interface for the class 
//PFArrayDBak. Objects of this type are partially filled arrays of doubles.
//This version allows the programmer to make a backup copy and restore
//to the last saved copy of the partially filled array.
#ifndef PFARRAYDBAK_H
#define PFARRAYDBAK_H
#include "pfarrayd.h"

class PFArrayDBak : public PFArrayD
{
public:
    PFArrayDBak( );
    //Initializes with a capacity of 50.

    PFArrayDBak(int capacityValue);

    PFArrayDBak(const PFArrayDBak& Object);

    void backup( );
    //Makes a backup copy of the partially filled array.

    void restore( );
    //Restores the partially filled array to the last saved version. 
    //If backup has never been invoked, this empties the partially filled array.

    PFArrayDBak& operator =(const PFArrayDBak& rightSide);

    ~PFArrayDBak( );
private:
    double *b; //for a backup of main array.
    int usedB; //backup for inherited member variable used.
};

#endif //PFARRAYD_H

