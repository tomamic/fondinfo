#include <iostream>
using std::cout;
using std::endl;

//Class for a pair of values of type T:
template<class T>
class Pair
{
public:
    Pair( );
    Pair(T firstValue, T secondValue);
    void setFirst(T newValue);
    void setSecond(T newValue);
    T getFirst( ) const;
    T getSecond( ) const;
private:
    T first;
    T second;
};

template<class T>
Pair<T>::Pair(T firstValue, T secondValue)
{
    first = firstValue;
    second = secondValue;
}

template<class T>
void Pair<T>::setFirst(T newValue)
{
    first = newValue;
}

template<class T>
T Pair<T>::getFirst( ) const
{
    return first;
}

int main( )
{
    Pair<char> p('A', 'B');
    cout << "First is " << p.getFirst( ) << endl;
    p.setFirst('Z');
    cout << "First changed to " << p.getFirst( ) << endl;
 
    return 0;
}