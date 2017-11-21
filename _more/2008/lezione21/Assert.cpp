#include <cassert>
#include <stdlib.h>

const int MAX_P = 10;

int someMethod( int p1, int p2)
{
  assert ( (p1 > 0) && "You must have at least one client");
  assert ( (p2 >= 0) && (p2 <= MAX_P) ); 

  return 0;
}

int main()
{
  someMethod(-4, 0);

  system("pause");
  return 0;
}
