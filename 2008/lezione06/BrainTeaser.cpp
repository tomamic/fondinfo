// H. Sutter - Exceptional C++ - Addison Wesley

// Item 43: Const-correctness (Difficulty: 6)
// const is a powerful tool for writing safer code. Use const as much as 
// possible, but no more. Here are some obvious and not-so-obvious places 
// where const should - or shouldn't - be used.
// Don't comment on or change the structure of this program; it's contrived and 
// condensed for illustration only. Just add or remove const (including minor 
// variants and related key-words) wherever appropriate.
//   Bonus question: In what places are the program's results 
//   undefined/uncompilable due to const errors?

class Polygon
{
public:
  Polygon() : area_(-1) {}
  void AddPoint( const Point pt ) { InvalidateArea();
                                                      points_.push_back(pt); }
  Point GetPoint( const int i )       { return points_[i]; }
  int GetNumPoints()                    { return points_.size(); }
  double GetArea()
  {
    if ( area_ < 0 ) // if not yet calculated and cached
    {
      CalcArea(); // calculate now
    }
    return area_;
  }
private:
  void InvalidateArea() { area_ = -1; }
  void CalcArea()
  {
    area_ = 0;
    vector<Point>::iterator i;
    for ( i = points_.begin(); i != points_.end(); ++i )
      area_ += /* some work */;
  }
  vector<Point> points_;
  double area_;
};

Polygon operator+( Polygon& lhs, Polygon& rhs )
{
  Polygon ret = lhs;
  int last = rhs.GetNumPoints();
  for ( int i = 0; i < last; ++i ) // concatenate
  {
    ret.AddPoint( rhs.GetPoint(i) );
  }
  return ret;
}

void f( const Polygon& poly )
{
  const_cast<Polygon&>(poly).AddPoint( Point(0,0) );
}

void g( Polygon& const rPoly ) { rPoly.AddPoint( Point(1,1) ); }

void h( Polygon* const pPoly ) {pPoly->AddPoint( Point(2,2) ); }

int main()
{
  Polygon poly;
  const Polygon cpoly;
  f(poly);
  f(cpoly);
  g(poly);
  h(&poly);
}
