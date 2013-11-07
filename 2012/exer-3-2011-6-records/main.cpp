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

    ifstream in("../exer-3-2011-6-records/list.txt");

    // alternative solution, without istringstream
//    getline(in, name, ':');
//    in >> points;
//    getline(in, remaining);  // consume the newline!
//    while (in.good()) {
//        records[name] = points;
//        getline(in, name, ':');
//        in >> points;
//        getline(in, remaining);
//    }

    while (getline(in, line)) {
        istringstream line_stream(line);
        getline(line_stream, name, ':');
        line_stream >> points;

        records[name] = points;
    }

    // in. pro: CONFIG += c++11
    for (auto i : records) {
        clog << i.first << ": " << i.second << endl;
    }

    string username;
    cout << "User?" << endl;
    while (getline(cin, username)) {
        if (records.count(username))
            cout << records[username] << endl;
        else cout << "Unknown user" << endl;
        cout << "User?" << endl;
    }

    return 0;
}
