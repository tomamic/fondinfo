//This is the header file dtime.h. This is the interface for the class DigitalTime.
//Values of this type are times of day. The values are input and output in
//24 hour notation as in 9:30 for 9:30 AM and 14:45 for 2:45 PM.

#ifndef DTIME_H
#define DTIME_H

#include <iostream>
using namespace std;

class DigitalTime
{
public:
    DigitalTime(int theHour, int theMinute);
    DigitalTime( );
    //Initializes the time value to 0:00 (which is midnight).

    int getHour( ) const;
    int getMinute( ) const;
    void advance(int minutesAdded);
    //Changes the time to minutesAdded minutes later.

    void advance(int hoursAdded, int minutesAdded);
    //Changes the time to hoursAdded hours plus minutesAdded minutes later.

    friend bool operator ==(const DigitalTime& time1, 
                            const DigitalTime& time2);

    friend istream& operator >>(istream& ins, DigitalTime& theObject);

    friend ostream& operator <<(ostream& outs, const DigitalTime& theObject);

private:
  
    int hour;
    int minute;
 
    static void readHour(int& theHour);
    //Precondition: Next input in to be read from the keyboard is 
    //a time in notation, like 9:45 or 14:45.
    //Postcondition: theHour has been set to the hour part of the time. 
    //The colon has been discarded and the next input to be read is the minute.

    static void readMinute(int& theMinute);
    //Reads the minute from the keyboard after readHour has read the hour.

    static int digitToInt(char c);
    //Precondition: c is one of the digits ’0’ through ’9’.
    //Returns the integer for the digit; that is, digitToInt(’3’) returns 3.

};


#endif //DTIME_H
