#ifndef ElementList_h
#define ElementList_h

#include <iostream>

class ElementList{
public:
  ElementList(int day = 0, int hour = 0);
  int getDay() const { return day_; }
  int getHour() const { return hour_; }
  friend std::ostream& operator << (std::ostream& outputStream, const ElementList& elList);
private:
  int day_;
  int hour_;
};

bool operator==(const ElementList& elList1, const ElementList& elList2);
bool operator<(const ElementList& elList1, const ElementList& elList2);

#endif 
