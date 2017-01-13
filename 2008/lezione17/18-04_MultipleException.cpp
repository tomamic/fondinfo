#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;

class NegativeNumber
{
public:
    NegativeNumber( ){}
    NegativeNumber(string theMessage): message(theMessage) {}
    string getMessage( ) const { return message; }
private:
    string message;
};

class DivideByZero
{};

int main( )
{
    int pencils, erasers;
    double ppe; //pencils per eraser

    try
    {
        cout << "How many pencils do you have?\n";
        cin >> pencils;
        if (pencils < 0)
             throw NegativeNumber("pencils");

        cout << "How many erasers do you have?\n";
        cin >> erasers;
        if (erasers < 0)
            throw NegativeNumber("erasers");

         if (erasers != 0)
            ppe = pencils/static_cast<double>(erasers);
        else
            throw DivideByZero( );

        cout << "Each eraser must last through " 
             << ppe << " pencils.\n";
    }
    catch(NegativeNumber e)
    {
       cout << "Cannot have a negative number of "
            << e.getMessage( ) << endl;
    }
    catch(DivideByZero)
    {
       cout << "Do not make any mistakes.\n";
    }

    cout << "End of program.\n";
    return 0;
}
