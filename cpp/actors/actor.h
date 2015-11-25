#ifndef ACTOR_H
#define ACTOR_H


class Actor
{
public:
    virtual void move() = 0;
    virtual int get_x() = 0;
    virtual int get_y() = 0;

    // a virtual descructor is necessary, if
    // subclasses may have their own destructors
    virtual ~Actor() {}
};

#endif // ACTOR_H
