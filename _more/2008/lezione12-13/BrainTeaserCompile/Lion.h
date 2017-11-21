#ifndef Lion_h
#define Lion_h

#include "Animal.h"

class Lion: public Animal
{
 public:
  Lion ( const int = 0, const int = 0);

  void print() const;
};

#endif
