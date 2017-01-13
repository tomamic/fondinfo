#include <cstdlib>
#include <iostream>

#include <set>

#include "ElementSet.h"

using namespace std;

void printElementIterator( const set<ElementSet>::const_iterator pos, const set<ElementSet>& mySet);
void printSet( const std::set< ElementSet > &setRef );

int main()
{
  // Empty Set Container
  set<ElementSet> mySet;
	
  // Insert Elements in random order);
  mySet.insert( ElementSet(3,4) );
  mySet.insert( ElementSet(3,2) );
  mySet.insert( ElementSet(9,6) );
  mySet.insert( ElementSet(2,3) );
  mySet.insert( ElementSet(9,4) );
  mySet.insert( ElementSet(2,4) );

  printSet(mySet);

  // needs operator<
  mySet.erase( ElementSet(3,4) );
  printSet(mySet);

  // needs operator<
  mySet.erase( 3 );
  printSet(mySet);

  // needs operator<
  set<ElementSet>::const_iterator findPos = mySet.find( ElementSet(3,2) );
  printElementIterator(findPos, mySet);

  findPos = mySet.find( ElementSet(3,4) );
  printElementIterator(findPos, mySet);


  return EXIT_SUCCESS;	
	
}

void printElementIterator( const set<ElementSet>::const_iterator pos, const set<ElementSet>& mySet)
{
  if ( pos != mySet.end() )
    cout << "Looking for: " << *pos << endl;
  else
    cout << "Element not Found" << endl;
}


void printSet( const std::set< ElementSet > &setRef )
{
  if ( setRef.empty() )
    cout << "List is empty";
  else 
  {
    std::set< ElementSet >::const_iterator pos;
    for (pos = setRef.begin(); pos != setRef.end(); ++pos) 
    {
      cout << *pos;
    }
    cout << endl;
  } 
} 
