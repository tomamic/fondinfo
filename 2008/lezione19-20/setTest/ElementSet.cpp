#include "ElementSet.h"

ElementSet::ElementSet(int day, int hour)
: day_(day), hour_(hour)
{}


bool operator<(const ElementSet& elSet1, const ElementSet& elSet2)
{
  if ( elSet1.getDay() < elSet2.getDay() )
    return true;
  else
    if ( elSet1.getDay() > elSet2.getDay() )
      return false;
    else
      if ( elSet1.getHour() < elSet2.getHour() )
        return true;
      else 
	return false;
}

/*
bool operator<(const ElementSet& elSet1, const ElementSet& elSet2)
{
  if ( elSet1.getDay() < elSet2.getDay() )
    return true;
  else
    return false;
}
*/
 

std::ostream& operator<< (std::ostream& outputStream, const ElementSet& elSet)
{

  outputStream << "Date: " << elSet.day_ << " Hour: " << elSet.hour_ << std::endl;
  return outputStream;
	
}
