/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <iostream>
#include <vector>

using namespace std;

class Animal {
public:
    virtual void say() = 0;
};

class Dog : public Animal {
    string name_;
public:
    Dog(string name) { name_ = name; }
    void say() {
        cout << "I am " << name_ << " Dog. I say: WOOF!" << endl;
    }
};

class Cat : public Animal {
    string name_;
public:
    Cat(string name) { name_ = name; }
    void say() {
        cout << "I am " << name_ << " Cat. I say: MEOW!" << endl;
    }
};

class Pig : public Animal {
    string name_;
public:
    Pig(string name) { name_ = name; }
    void say() {
        cout << "I am " << name_ << " Pig. I say: OINK!" << endl;
    }
};

int main() {
    auto d = Dog("Danny");
    auto c = Cat("Candy");
    auto p1 = Pig("Peppa");
    auto p2 = Pig("George");

    // a list of (ptrs to) Animal objects
    vector<Animal*> animals = {&d, &c, &p1, &p2};

    for (auto a : animals) {
        a->say();
    }
}
