#include <iostream>

using std::cout;
using std::endl;

#include "Dog.h"

Dog::Dog( const int h, const int w, string n )
  : Animal( h, w )
{
  setName( n );
}

void Dog::setName(const char* n)
{
  n = name;
}

void Dog::Print() const
{
  cout << "This animal is a dog, its name is: " << name << endl;

  print();
}
