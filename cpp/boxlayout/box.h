#ifndef BOX_H
#define BOX_H

class Box
{
public:
    Box(int width, int heigth);
    int width() const;
    int height() const;
    int area() const;
    int perimeter() const;

private:
    int width_;
    int height_;
};

#endif // BOX_H
