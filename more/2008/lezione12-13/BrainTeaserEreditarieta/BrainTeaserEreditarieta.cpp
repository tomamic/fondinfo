//---------------> Animal.h

#ifndef Animal_h
#define Animal_h

#include <string>

using std::string;

class Animal 
{
 public:
  Animal( const int = 0, const int = 0 );

  void setHeight( int );
  int getHeight() const;

  void setWeight( int );
  int getWeight() const;

  string getName() const;
  void print() const;

 private:
  int height;
  int weight;

};

#endif


//---------------> Animal.cpp

#include <iostream>
#include "Animal.h"

using std::cout;
using std::endl;

Animal::Animal( const int h, const int w )
{
  height = h;
  weight = w;
}

void Animal::print() const
{
  cout << "This animal's height and weight are as follows\n"
       << "Height:" << height << "\tWeight: " << weight
       << endl << endl;
}

int Animal::getHeight() const
{
  return height;
}

int Animal::getWeight() const
{
  return weight;
}

void Animal::setHeight( const int h )
{
  height = h;
}

void Animal::setWeight( const int w )
{
  weight = w;
}

string Animal::getName() const
{
  return name;
}


//---------------> Dog.h

#ifndef Dog_h
#define Dog_h

class Dog: public Animal 
{
 public:
  Dog( const int, const int, string = "Toto");

  void print() const;
  void setName( string );
 private:
  string name;
};

#endif


//-----------------> Dog.cpp

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


//----------------> Lion.h
#ifndef Lion_h
#define Lion_h

#include "Animal.h"

class Lion
{
 public:
  Lion ( const int = 0, const int = 0);

  void print() const;
};

#endif


//----------------> Lion.cpp

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
  print();
}




//--------------> main.cpp

#include <iostream>

using std::cout;
using std::endl;

#include "Animal.h"
#include "Lion.h"

int main()
{
  Animal a1( 0, 0 );
  Dog d1( 60, 120, "Fido" );
  Dog d2;
  Lion lion1( 45, 300 );
  a1.print();
  d1.print();
  d2.print();
  lion1.print();

  a1 = d1;
  cout << "Animal 1 now has the same height and weight "
       << "as dog 1\n";

  a1.print();

  d2 = a1;
  cout << "Dog 2 now has the same height and weight as animal 1\n"
  d2.print();

  return 0;

}
