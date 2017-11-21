// H. Sutter - Exceptional C++ - Addison Wesley

// Item 20: Class Mechanics  (Difficulty: 7)
// How good are you at the details of writing classes? 
// This item focuses not only on blatant errors,
// but even more so on professional style. 
// Understanding these principles will help you to design
// classes that are more robust and easier to maintain.

// You are doing a code review. A programmer has written the following class, 
// which shows some poor style and has some real errors. 
// How many can you find, and how would you fix them?

class Complex
{
public:
  Complex( double real, double imaginary = 0 )
    : _real(real), _imaginary(imaginary)
  {
  }
  
  void operator+ ( Complex other )
  {
    _real = _real + other._real;
    _imaginary = _imaginary + other._imaginary;
  }
  
  void operator<<( ostream os )
  {
    os << "(" << _real << "," << _imaginary << ")";
  }
  
  Complex operator++()
  {
    ++_real;
    return Complex(_real, _imaginary);
  }
  
  Complex operator++( int )
  {
    Complex temp(_real, _imaginary);
    ++_real;
    return temp;
  }
  private:
    double _real, _imaginary;
};
