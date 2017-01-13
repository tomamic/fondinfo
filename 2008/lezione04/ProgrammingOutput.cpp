// Per ognuno di questi segmenti di programma, leggere il codice e scrivete l'output

//---------------------- Time class

class Time
{
public:
  Time();
  void setTime(int, int, int); // set hour, minute, second
  void printUniversal();       // print universal time format
  void printStandard();        // print standard time format

private:
  int hour;   // 0 - 23 (24-hour clock format)
  int minute; // 0 - 59
  int second; // 0 - 59
};

// Time constructor initializes each data member to zero.
// Ensures all Time objects start in a consistent state
Time::Time()
{
  hour = minute = second = 0;
}

// Set a new Time value using universal time. Perform validity
// checks on the data value. Set invalid values to zero.
void Time::setTime(int h, int m, int s)
{
  hour = ( h >= 0 && h < 24 ) ? h : 0;
  minute = ( m >= 0 && m < 60 ) ? m : 0;
  second = ( s >= 0 && s < 60 ) ? s : 0;
}

// Print Time in universal format
void Time::printUniversal()
{
  cout << setfill('0') << setw(2) << hour << ":"
       << setw(2) << minute << ":"
       << setw(2) << second;
}

// Print Time in standard format
void Time::printStandard()
{
  cout << ((hour == 0 || hour == 12) ? 12 : hour % 12)
       << ":" << setfill('0') << setw(2) << minute
       << ":" << setw(2) << second
       << (hour < 12 ? "AM" : "PM");
}


//----------------- Qual e` l'output del seguente pezzo di programma?

Time t1();

t1.setTime(18, 22, 9);
cout << "The time is: ";
t1.printStandard();


//----------------- Qual e` l'output del seguente pezzo di programma?  

Time t(3, 4, 5);

t.printStandard();
cout << endl;

t.printUniversal();
cout << endl;

t.setTime(99, 3, 4);

t.printUniversal();
cout << endl;


//------------------  Qual e` l'output del programma che segue?
#include <iostream>

using std::cout;
using std::endl;

class M 
{
public:
  M(int);
  int mystery(int);

private:
  int data;
  double number;
};

M::M(int q)
{
  data = q;
  number = .5;
}

int M::mystery(int q)
{
  data += q;
  return static_cast<int>(data * number);
}

int main()
{
  M stuff(44);
  cout << stuff.mystery(78);

  return 0;
}


//--------------------------- Qual e` l'output del programma che segue?

#include <iostream>
using std::cout;
using std::endl;

class M
{
public:
  M(int);
  int mystery(int);

private:
  int data;
  int number;
};

M::M(int q = 0)
{
  data = q;
  number = 2;
}

int M::mystery(int q)
{
  data += q;
  return data;
}

int main()
{
  M mObject(2);
  M *mPtr = &mObject;

  cout << mObject.mystery(20) << endl;
  cout << mPtr->mystery(30);

  return 0;
}
