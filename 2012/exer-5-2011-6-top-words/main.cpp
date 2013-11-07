/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string word1, string word2) {
    return word1.size() > word2.size();
}

int main(int argc, char *argv[])
{
    vector<string> fileNames;
    vector<string> words;

    string fileName;
    cout << "Filename?" << endl;
    getline(cin, fileName);
    while (fileName != "") {

        fileNames.push_back(fileName);

        cout << "Filename?" << endl;
        getline(cin, fileName);
    }

    cout << "How many top words?" << endl;
    int n;
    cin >> n;

    for (int i = 0; i < fileNames.size(); ++i) {
        ifstream in(fileNames[i].c_str());

        string word;
        while (in >> word) {
            if (count(words.begin(), words.end(), word) == 0) {
                words.push_back(word);
            }
        }
    }

    sort(words.begin(), words.end(), compare);

    for (int i = 0; i < words.size() && i < n; ++i) {
        cout << words[i] << endl;
    }

    return 0;
}
