#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// const vector<string> OPERATORS = {"+", "-", "*", "/", "div", "mod"};
// C++2011 assignment, add the following line in .pro file
// QMAKE_CXXFLAGS += -std=c++0x

const string OPERATORS[] = {"+", "-", "*", "/", "div", "mod"};

void writeInfix(istream& in, ostream& out)
{
    string op; in >> op;

    if (count(OPERATORS, OPERATORS + 6, op) > 0) {
        out << "(";
        writeInfix(in, out);
        out << ' ' << op << ' ';
        writeInfix(in, out);
        out << ")";
    } else {
        out << op;
    }
}

float eval(istream& in)
{
    float result = 0, a = 0, b = 0;
    string op; in >> op;

    if (count(OPERATORS, OPERATORS + 6, op) > 0) {
        a = eval(in);
        b = eval(in);

        if (op == "+") result = a + b;
        else if (op == "-") result = a - b;
        else if (op == "*") result = a * b;
        else if (op == "/") result = a / b;
        else if (op == "div") result = int(a) / int(b);
        else if (op == "mod") result = int(a) % int(b);
    } else {
        istringstream(op) >> result;
    }
    return result;
}

int main()
{
    string expr = "mod + * + 1 2 + 2 3 4 5";

    istringstream in1(expr);
    writeInfix(in1, cout);

    istringstream in2(expr);
    cout << " = " << eval(in2) << endl;

    // ((((1 + 2) * (2 + 3)) + 4) mod 5) = 4
    return 0;
}
