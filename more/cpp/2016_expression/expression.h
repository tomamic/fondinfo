#ifndef EXPRESSION_H
#define EXPRESSION_H


class Expression
{
public:
    virtual float eval() = 0;
    virtual std::string prefix() = 0;
};

#endif // EXPRESSION_H
