// Fig. 19.1: fig19_01.cpp
// Demonstrating string assignment and concatenation
#include <iostream>

using std::cout;
using std::endl;

#include <string>

using std::string;

int main()
{
   string s1( "cat" ), s2, s3;

   s2 = s1;          // assign s1 to s2 with =
   s3.assign( s1 );  // assign s1 to s3 with assign()
   cout << "s1: " << s1 << "\ns2: " << s2 << "\ns3: "
        << s3 << "\n\n";

   // modify s2 and s3 
   s2[ 0 ] = s3[ 2 ] = 'r';

   cout << "After modification of s2 and s3:\n"
        << "s1: " << s1 << "\ns2: " << s2 << "\ns3: ";             

   // demonstrating member function at()
   int len = s3.length();
   for ( int x = 0; x < len; ++x ) 
      cout << s3.at( x );

   // concatenation
   string s4( s1 + "apult" ), s5;  // declare s4 and s5

   // overloaded +=
   s3 += "pet";             // create "carpet"
   s1.append( "acomb" );    // create "catacomb"

   // append subscript locations 4 thru the end of s1 to
   // create the string "comb" (s5 was initially empty)
   s5.append( s1, 4, s1.size() );
                                 
   cout << "\n\nAfter concatcenation:\n" << "s1: " << s1 
        << "\ns2: " << s2 << "\ns3: " << s3 << "\ns4: " << s4 
        << "\ns5: " << s5 << endl;
   
   return 0;
}


/**************************************************************************
 * (C) Copyright 2000 by Deitel & Associates, Inc. and Prentice Hall.     *
 * All Rights Reserved.                                                   *
 *                                                                        *
 * DISCLAIMER: The authors and publisher of this book have used their     *
 * best efforts in preparing the book. These efforts include the          *
 * development, research, and testing of the theories and programs        *
 * to determine their effectiveness. The authors and publisher make       *
 * no warranty of any kind, expressed or implied, with regard to these    *
 * programs or to the documentation contained in these books. The authors *
 * and publisher shall not be liable in any event for incidental or       *
 * consequential damages in connection with, or arising out of, the       *
 * furnishing, performance, or use of these programs.                     *
 *************************************************************************/
