/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    string line, name, remaining;
    int points;

    map<string, int> records;

    ifstream in("../2011-e3-6-records/list.txt");

//    getline(in, name, ':');
//    in >> points;
//    getline(in, remaining);
//    while (in.good()) {
//        records[name] = points;
//        getline(in, name, ':');
//        in >> points;
//        getline(in, remaining);
//    }

    getline(in, line);
    while (in.good()) {

        istringstream lineStream(line);

        getline(lineStream, name, ':');
        lineStream >> points;

        clog << name << ": " << points << endl;
        records[name] = points;

        getline(in, line);
    }

    // a taste of C++11 - add this line in .pro:
    // QMAKE_CXXFLAGS += -std=c++11
//    for (auto i : records) {
//        clog << i.first << ": " << i.second << endl;
//    }

    string userName;
    cout << "User?" << endl;
    getline(cin, userName);
    while (cin.good()) {
        if (records.count(userName)) cout << records[userName] << endl;
        else cout << "Unknown user" << endl;
        cout << "User?" << endl;
        getline(cin, userName);
    }

    return 0;
}
