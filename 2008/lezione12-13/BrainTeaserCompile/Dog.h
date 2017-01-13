#ifndef Dog_h
#define Dog_h

#include "Animal.h"


class Dog: public Animal 
{
 public:
  Dog( const int = 0 , const int = 0, string = "Toto");

  void print() const;
  void setName( string );
 private:
  string name;
};

#endif
