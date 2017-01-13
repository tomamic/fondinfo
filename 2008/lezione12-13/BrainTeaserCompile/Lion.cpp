#include <iostream>

using std::cout;
using std::endl;

#include "Lion.h"

Lion::Lion( const int h, const int w)
  : Animal(h, w)
{}

void Lion::print() const
{
  cout << "this animal is a lion\n";
  Animal::print();
}
