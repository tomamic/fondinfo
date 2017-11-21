//This is the header file pfarray.h. This is the interface for the class 
//PFArray. Objects of this type are partially filled arrays with base type T.
#ifndef PFARRAY_H
#define PFARRAY_H

namespace PFArraySavitch
{ 
      template <class T >
    class PFArray
    {
    public:
        PFArray( ); //Initializes with a capacity of 50.

        PFArray(int capacityValue);

        PFArray(const PFArray<T>& pfaObject);

        void addElement(T element);
        //Precondition: The array is not full.
        //Postcondition: The element has been added.

        bool full( ) const; //Returns true if the array is full, false otherwise.

        int getCapacity( ) const;

        int getNumberUsed( ) const;

        void emptyArray( );
        //Resets the number used to zero, effectively emptying the array.

        T& operator[](int index);
        //Read and change access to elements 0 through numberUsed - 1.

        PFArray<T>& operator =(const PFArray<T>& rightSide);

        virtual ~PFArray( );
    private:
        T *a; //for an array of T.
        int capacity; //for the size of the array.
        int used; //for the number of array positions currently in use.
    };
    
}// PFArraySavitch
#endif //PFARRAY_H
