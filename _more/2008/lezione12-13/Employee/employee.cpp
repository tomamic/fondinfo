//This is the file: employee.cpp 
//This is the implementation for the class Employee.
//The interface for the class Employee is in the header file employee.h.
#include <string>
#include <cstdlib>
#include <iostream>
#include "employee.h"
using std::string;
using std::cout;

namespace SavitchEmployees
{
    Employee::Employee( ) : name("No name yet"), ssn("No number yet"), netPay(0)
    {
        //deliberately empty
    }

    Employee::Employee(string theName, string theNumber) 
       : name(theName), ssn(theNumber), netPay(0) 
    {			
        //deliberately empty
    }

    string Employee::getName( ) const 
    {
        return name;
    }

    string Employee::getSsn( ) const 
    {
        return ssn;
    }

    double Employee::getNetPay( ) const 
    {
        return netPay;
    }

   void Employee::setName(string newName)
    {
        name = newName;
    }

    void Employee::setSsn(string newSsn)
    {
        ssn = newSsn;
    }

    void Employee::setNetPay (double newNetPay)
    {
        netPay = newNetPay;
    }

    void Employee::printCheck( ) const
    {
        cout << "\nERROR: printCheck FUNCTION CALLED FOR AN \n"
             << "UNDIFFERENTIATED EMPLOYEE. Aborting the program.\n" 
             << "Check with the author of the program about this bug.\n";
        exit(1);
    }

}//SavitchEmployees




    