#ifndef TENTSPUZZLE_H
#define TENTSPUZZLE_H

#include <string>
#include <vector>

class TentsPuzzle {
public:
    TentsPuzzle();                  // default board
    void place_tent(int x, int y);  // take a move
    std::string str();              // string representation
    bool solved();                  // is puzzle solved?
    // TentsPuzzle(istream& in);    // read from stream
    // bool wrong();                // are tents misplaced?
    char get(int x, int y);
    int rows();
    int cols();

    static const char EMPTY = ' ';
    static const char OUT = '!';
    static const char TENT = 'A';
    static const char TREE = 'T';
private:
    int count_row(int y);
    int count_col(int x);
    int count_around(int x, int y);
    // void set(int y, int x, char value);

    int cols_ = 5;
    int rows_ = 5;
    std::vector<char> board_ = {' ', 'T', ' ', ' ', ' ',
                                ' ', ' ', ' ', ' ', 'T',
                                ' ', 'T', ' ', 'T', ' ',
                                ' ', ' ', ' ', ' ', 'T',
                                ' ', ' ', ' ', ' ', ' '};
    std::vector<int> col_constraints_ = {2, 0, 1, 0, 2};
    std::vector<int> row_constraints_ = {2, 0, 2, 0, 1};
};

#endif // TENTSPUZZLE_H
