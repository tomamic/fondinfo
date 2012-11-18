/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

const int N = 10000;
const int DIE_FACES = 6;
const int ATTACK_DICE = 3;
const int DEFENCE_DICE = 2;

bool compare(char x, char y)
{
    return x > y;
}

void rollDice(vector<char>& dice)
{
    for (int i = 0; i < dice.size(); ++i) {
        dice[i] = '1' + (rand() % DIE_FACES);
    }
    sort(dice.begin(), dice.end(), compare);
    // without an ad-hoc compare function...
    // reverse(dice.begin(), dice.end());
}

int attackResult(vector<char>& a, vector<char>& d)
{
    int attack = 0;
    for (int i = 0; i < min(a.size(), d.size()); ++i) {
        // without an ad-hoc compare function, you could
        // also invert the game rules here: a[i] < d[i]
        if (a[i] > d[i]) ++attack;
    }
    return attack;
}

int main(int argc, char *argv[])
{
    srand(time(NULL));
    // attacker rolls ATTACK_DICE dice
    vector<char> attack(ATTACK_DICE);
    // defender rolls DEFENCE_DICE dice
    vector<char> defence(DEFENCE_DICE);

    // associate a possible attack result (0, 1, 2, ...)
    // with its actually counted occurrences
    vector<int> resultOccurrences(min(ATTACK_DICE, DEFENCE_DICE) + 1);

    for (int x = 0; x < N; ++x) {
        rollDice(attack);
        cout << "a: " << string(attack.begin(), attack.end()) << endl;
        rollDice(defence);
        cout << "d: " << string(defence.begin(), defence.end()) << endl;
        int result = attackResult(attack, defence);
        cout << "result: " << result << endl << endl;

        ++resultOccurrences[result];
    }

    for (int j = 0; j < resultOccurrences.size(); ++j) {
        cout << j << ": " << 100.0 * resultOccurrences[j] / N << endl;
    }

    return 0;
}
