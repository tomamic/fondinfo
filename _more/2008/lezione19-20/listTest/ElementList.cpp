#include "ElementList.h"

ElementList::ElementList(int day, int hour)
: day_(day), hour_(hour)
{}


bool operator==(const ElementList& elList1, const ElementList& elList2)
{
  if ( ( elList1.getDay() == elList2.getDay() ) && 
       ( elList1.getHour() == elList2.getHour() ) )
     return true;
  else
     return false;
}


/*
bool operator==(const ElementList& elList1, const ElementList& elList2)
{
  if (  elList1.getDay() == elList2.getDay()  )
    return true;
  else
    return false;
}
*/
 
 

bool operator<(const ElementList& elList1, const ElementList& elList2)
{
  if ( elList1.getDay() < elList2.getDay() )
    return true;
  else
    if ( elList1.getDay() > elList2.getDay() )
      return false;
    else
      if ( elList1.getHour() < elList2.getHour() )
        return true;
      else 
        return false;
} 

std::ostream& operator<< (std::ostream& outputStream, const ElementList& elList)
{
  outputStream << "Date: " << elList.day_ << " Hour: " << elList.hour_ << std::endl;
	
  return outputStream;
}

