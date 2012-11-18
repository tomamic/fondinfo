/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
    const int MAX = 90;
    int secret, guess, tries = 0;

    /* initialize the seed for random numbers */
    srand ( time(NULL) );

    /* generate the secret number */
    secret = (rand() % MAX) + 1;

    do {
        cout << "Guess the number (1-90): ";
        cin >> guess;

        ++tries;

        if (secret < guess) {
            cout << "The secret is smaller than " << guess << endl;
        } else if (secret > guess) {
            cout << "The secret is larger than " << guess << endl;
        } else {
            cout << "Congratulations, you guessed in " << tries << " tries" << endl;
        }
    } while (secret != guess && tries <= 10);

    return 0;
}
