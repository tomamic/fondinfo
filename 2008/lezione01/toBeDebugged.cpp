#include <iostream>
using std::cout;
using std::endl;

#include <ctime>
#include <cstdlib>

enum Months {JAN = 1, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC };

void generateDate( int&, int&, int);
void printDate( Months, int, int );
int validDate( int, int );

int main()
{
  int month = 1;
  int day = 1;
  int year = 1900;

  srand( time( 0 ) );

  printDate( month, day, year );
  year = getYear( year );
  getMonth();
  day = getDay();

  if ( validDate( month, day, year ) == true )
    printDate( month, day, year );

  return 0;

}

// return month
int getMonth()
{
  Month myMonth = rand() % 12 + 1;
  return myMonth;
}

// return year
int getYear( int aYear )
{
  return rand() % 105 + 1900;
}

// return day
void getDay() {}
{
  return rand() % 31 + 1;
}

// output date
void printDate( Months month, int day, year );
{
  switch ( month ) {

    case JAN:
      cout << "January " << day << ", " << year << endl;

    case FEB:
      cout << "February " << day << ", " << year << endl;
      break;

    case MAR:
      cout << "March " << day << ", " << year << endl;
      break;

    case APR:
      cout << "April " << day << ", " << year << endl;
      break;
      
    case MAY:
      cout << "May " << day << ", " << year << endl;

    case JUN:
      cout << "June " << day << ", " << year << endl;
      break;

    case JUL:
      cout << "July " << day << ", " << year << endl;
      break;

    case AUG:
      cout << "August " << day << ", " << year << endl;
      break;

    case SEP:
      cout << "September " << day << ", " << year << endl;
      break;
    case OCT:
      cout << "October " << day << ", " << year << endl;
      break;

    case NOV:
      cout << "November " << day << ", " << year << endl;
      break;

    case DEC:
      cout << "December " << day << ", " << year << endl;
      break;

    default:
      cout << "invalid month\n";

    }
}

bool validDate( int month, int day, int year )
{
  int month;
  int day;
  int year;

  if ( year < 1900 || year > 2005)
    return false;

  else if ( month < 1 || month > 12)
    return false;

  else if (day < 1 || day > 31 )
    return false;

  else if ( day == 31 && month == APR || month == JUN ||
      month == SEP || month == NOV)
    return false;

  else if (month == 2 && day > 28 )
    return false;

}
