#ifndef ElementSet_h
#define ElementSet_h

#include <iostream>

class ElementSet{
public:
  ElementSet(int day = 0, int hour = 0);
  int getDay() const { return day_; }
  int getHour() const { return hour_; }
  friend std::ostream& operator << (std::ostream& outputStream, const ElementSet& elSet);
private:
  int day_;
  int hour_;
};

bool operator<(const ElementSet& elSet1, const ElementSet& elSet2);
#endif 
