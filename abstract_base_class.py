'''
abstract classes doesnt have its own implementations as well
as you can not create objects for abstract base class.
ABC class used for making sure its derived classes, methods must and should
implement the functionality which given by ABC class
'''
from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
    # this make sures every dervide class must implememt area method,
    # if not implememted it throws an Error..
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of a square is: ", (self.side)*(self.side))

class Rectangle(Shape):
    width=5
    length=10
    def area(self):
        print("Area of a rectange is: ", (4*self.width)+(4*self.length))

square = Square()
rectangle = Rectangle()
# shape = Shape() --> doesnt work..

square.area()
rectangle.area()
