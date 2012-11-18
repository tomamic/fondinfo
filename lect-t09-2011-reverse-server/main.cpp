/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
    while (getline(stream, line) && line != "." && line != ".\r") {
        if (line[line.size() - 1] == '\r') { line.resize(line.size() - 1); }
        clog << this_thread::get_id() << " req: " << line << endl;

        reverse(line.begin(), line.end());
        stream << line << endl;
    }
    delete &stream;
}

//void cleanup(vector<thread*>& threads)
//{
//    for (int i = threads.size() - 1; i >= 0; --i) {
//        if (! threads[i]->joinable()) {
//            delete threads[i];
//            threads.erase(threads.begin()+i);
//        }
//    }
//}

int main()
{
    //vector<thread*> threads;
    try {
        boost::asio::io_service io_service;
        tcp::endpoint endpoint(tcp::v4(), 4444);
        tcp::acceptor acceptor(io_service, endpoint);

        while (true) {
            tcp::iostream* socketStream = new tcp::iostream();
            // the buffer of the tcp::stream is associated
            // with the newly accepted socket
            acceptor.accept(*(socketStream->rdbuf()));

            // 1. serial code
            //reverseService(*socketStream);

            // 2. vector of thread ptrs, periodic cleanup needed
            //clenup(threads);
            //thread* t = new thread( [socketStream]{ reverseService(*socketStream); } )
            //threads.push_back(t);

            // 3. detached thread; the real thread will continue its
            // execution, independently from the c++ thread handle
            thread t( [socketStream]{ reverseService(*socketStream); } );
            t.detach();
        }
    } catch (exception& e) {
        cerr << e.what() << endl;
    }

    return 0;
}
