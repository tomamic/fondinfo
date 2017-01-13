#include <iostream>
#include <cstdlib>
using namespace std;

class DayOfYear
{
public:
    void input( );
    void output( );
    void set(int newMonth, int newDay);
    //Precondition: newMonth and newDay form a possible date.

    void set(int newMonth);
    //Precondition: 1 <= newMonth <= 12
    //Postcondition: The date is set to the first day of the given month.
 
    int getMonthNumber( ); //Returns 1 for January, 2 for February, etc.
    int getDay( );
private:
    int month;
    int day;
};

int main( )
{
    DayOfYear today, bachBirthday;
    cout << "Enter today's date:\n";
    today.input( );
    cout << "Today's date is ";
    today.output( );
    cout << endl;

    bachBirthday.set(3, 21);
    cout << "J. S. Bach's birthday is ";
    bachBirthday.output( );
    cout << endl;

        if ( today.getMonthNumber( ) == bachBirthday.getMonthNumber( ) &&
               today.getDay( ) == bachBirthday.getDay( ) )
        cout << "Happy Birthday Johann Sebastian!\n";
    else
        cout << "Happy Unbirthday Johann Sebastian!\n";

    return 0;
}

//Uses iostream and cstdlib:
void DayOfYear::set(int newMonth, int newDay)
{
    if ((newMonth >= 1) && (newMonth <= 12))
        month = newMonth;
    else
    {
        cout << "Illegal month value! Program aborted.\n";
        exit(1);
    }
    if ((newDay >= 1) && (newDay <= 31))
        day = newDay;
    else
    {
        cout << "Illegal day value! Program aborted.\n";
        exit(1);
    }
}

//Uses iostream and cstdlib:
void DayOfYear::set(int newMonth)
{
    if ((newMonth >= 1) && (newMonth <= 12))
        month = newMonth;
    else
    {
        cout << "Illegal month value! Program aborted.\n";
        exit(1);
    }
    day = 1;
}


int DayOfYear::getMonthNumber( )
{
    return month;
}

int DayOfYear::getDay( )
{
    return day;
}

//Uses iostream and cstdlib:
void DayOfYear::input( )
{
    cout << "Enter the month as a number: ";
    cin >> month;
    cout << "Enter the day of the month: ";
    cin >> day;
    if ((month < 1) || (month > 12) || (day < 1) || (day > 31))
    {
        cout << "Illegal date! Program aborted.\n";
        exit(1);
    }
}

void DayOfYear::output( )
{
    switch (month)
    {
        case 1:
            cout << "January "; break;
        case 2:
            cout << "February "; break;
        case 3:
            cout << "March "; break;
        case 4:
            cout << "April "; break;
        case 5:
            cout << "May "; break;
        case 6:
            cout << "June "; break;
        case 7:
            cout << "July "; break;
        case 8:
            cout << "August "; break;
        case 9:
            cout << "September "; break;
        case 10:
            cout << "October "; break;
        case 11:
            cout << "November "; break;
        case 12:
            cout << "December "; break;
        default:
            cout << "Error in DayOfYear::output. Contact software vendor.";
    }

    cout << day;
}





