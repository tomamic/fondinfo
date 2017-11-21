#include <iostream>

using std::cout;
using std::endl;

#include "Dog.h"

Dog::Dog( const int h, const int w, string n )
  : Animal( h, w )
{
  setName( n );
}

void Dog::setName(string n)
{
  name = n;
}

void Dog::print() const
{
  cout << "This animal is a dog, its name is: " << name << endl;

  Animal::print();
}
