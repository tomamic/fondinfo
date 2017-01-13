//This is the header file employee.h. 
//This is the interface for the class Employee.
//This is primarily intended to be used as a base class to derive
//classes for different kinds of employees.
#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <string>
using std::string;

namespace SavitchEmployees
{

    class Employee
    {
    public:
        Employee( );
        Employee(string theName, string theSsn);
        string getName( ) const;
        string getSsn( ) const;
        double getNetPay( ) const;
        void setName(string newName); 
        void setSsn(string newSsn);
        void setNetPay(double newNetPay);
        void printCheck( ) const;
    private:
        string name; 
        string ssn; 
        double netPay;
    };

}//SavitchEmployees

#endif //EMPLOYEE_H
