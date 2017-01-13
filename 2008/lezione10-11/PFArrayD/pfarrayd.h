//This is the HEADER FILE pfarrayd.h. This is the INTERFACE for the class 
//PFArrayD. Objects of this type are partially filled arrays of doubles.
#ifndef PFARRAYD_H
#define PFARRAYD_H

//Objects of this class are partially filled arrays of doubles.
class PFArrayD
{
public:
    PFArrayD( );
    //Initializes with a capacity of 50.

    PFArrayD(int capacityValue);

    PFArrayD(const PFArrayD& pfaObject);

    void addElement(double element);
    //Precondition: The array is not full.
    //Postcondition: The element has been added.

    bool full( ) const { return (capacity == used); }
    //Returns true if the array is full, false otherwise.

    int getCapacity( ) const { return capacity; }

    int getNumberUsed( ) const { return used; }

    void emptyArray( ){ used = 0; }
    //Empties the array.

    double& operator[](int index);
    //Read and change access to elements 0 through numberUsed - 1.

    PFArrayD& operator =(const PFArrayD& rightSide);

    ~PFArrayD( );
private:
    double *a; //for an array of doubles.
    int capacity; //for the size of the array.
    int used; //for the number of array positions currently in use.

};

#endif //PFARRAYD_H
