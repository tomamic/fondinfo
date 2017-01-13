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

  void print() const;

 private:
  int height;
  int weight;

};

#endif
