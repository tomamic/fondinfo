#include <cstdlib>
#include <iostream>


#include <list>

#include "ElementList.h"

using namespace std;

void printList( const std::list< ElementList > &listRef );

int main()
{
// Empty List Container
list<ElementList> myList;

// Insert Elements in random order);
myList.push_back( ElementList(3,4) );
myList.push_back( ElementList(3,2) );
myList.push_back( ElementList(9,6) );
myList.push_back( ElementList(2,3) );
myList.push_back( ElementList(9,4) );
myList.push_back( ElementList(2,4) );

printList(myList);
// needs operator==
myList.remove( ElementList(3,4) );
printList(myList);

// Create the tmp obj: ElementList(3), then remove
myList.remove( 3 );
printList(myList);

// needs operator<
myList.sort();
printList(myList);


return EXIT_SUCCESS;	
	
}


void printList( const std::list< ElementList > &listRef )
{
  if ( listRef.empty() )
    cout << "List is empty";
  else 
  {
    std::list< ElementList >::const_iterator pos;
    for (pos = listRef.begin(); pos != listRef.end(); ++pos) 
    {
      cout << *pos;
    }
    cout << endl;
  } 
}

