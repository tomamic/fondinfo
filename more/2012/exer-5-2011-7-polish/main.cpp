/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

void writeInfix(istream& in, ostream& out)
{
    string token;
    in >> token;

    float value = 0;
    istringstream numberParser(token);
    numberParser >> value;

    if (numberParser.fail()) {
        out << "(";
        writeInfix(in, out);
        out << ' ' << token << ' ';
        writeInfix(in, out);
        out << ")";
    } else {
        out << value;
    }
}

float eval(istream& in)
{
    string token;
    in >> token;

    float value = 0;
    istringstream numberParser(token);
    numberParser >> value;

    if (numberParser.fail()) {
        float a = eval(in);
        float b = eval(in);

        if (token == "+") value = a + b;
        else if (token == "-") value = a - b;
        else if (token == "*") value = a * b;
        else if (token == "/") value = a / b;
        else if (token == "div") value = int(a) / int(b);
        else if (token == "mod") value = int(a) % int(b);
    }
    return value;
}

int main()
{
    string expr = "mod + * + 1 2 + 2 3 4 5 ";

    istringstream in1(expr);
    writeInfix(in1, cout);

    istringstream in2(expr);
    cout << " = " << eval(in2) << endl;

    // ((((1 + 2) * (2 + 3)) + 4) mod 5) = 4
    return 0;
}
