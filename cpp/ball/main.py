import cppyy
cppyy.include("ball.hpp")
from cppyy.gbl import Ball

b = Ball(150, 200)
print(b.get_x(), b.get_y())
for i in range(10):
    b.move()
    print(b.get_x(), b.get_y())
