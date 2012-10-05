/**
* Example used in programming courses at University of Parma, IT.
* Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
*
* This software is free: you can redistribute it and/or modify it
* under the terms of the GNU General Public License, version 3 or
* later. See <http://www.gnu.org/licenses/>.
*/

#include <iostream>
#include <string>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;
using namespace std;

int main(int argc, char* argv[])
{
    try {
        tcp::iostream net("localhost", "4444");

        string req, ans;
        while (net && getline(cin, req)) {
            net << req << endl;
            getline(net, ans);
            cout << ans << endl;
        }
    } catch (exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }

    return 0;
}
