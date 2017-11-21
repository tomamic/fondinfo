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
