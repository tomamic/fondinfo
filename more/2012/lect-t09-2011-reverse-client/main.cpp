/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
