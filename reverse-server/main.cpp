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
#include <thread>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;
using namespace std;

void reverseService(iostream& stream)
{
    string line;
    while (getline(stream, line) && line != ".") {
        clog << this_thread::get_id() << " req: " << line << endl;
        reverse(line.begin(), line.end());
        stream << line << endl;
    }
    delete &stream;
}

int main()
{
    try {
        boost::asio::io_service io_service;
        tcp::endpoint endpoint(tcp::v4(), 4444);
        tcp::acceptor acceptor(io_service, endpoint);

        for (;;) {
            tcp::iostream* net = new tcp::iostream();
            acceptor.accept(*(net->rdbuf()));

            //reverseService(*stream);

            thread t( [net]{ reverseService(*net); } );
            t.detach();
        }
    } catch (exception& e) {
        cerr << e.what() << endl;
    }

    return 0;
}
