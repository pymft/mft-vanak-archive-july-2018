class Rectangle:
    def __init__(self, width, height):
        # print("an instance of class", self.__class__, "has been created")
        self.width = width
        self.height = height

    def area(self):
        # print("echo from parent")
        # print("method aread() from ", self.__class__, "has been called")
        return self.width * self.height

    def tell_your_geometric_type(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, a):
        # print("before super() being called from class ", self.__class__, "has been created")
        super().__init__(a, a)
        # print("after super() being called from class ", self.__class__, "has been created")
        # self.width = a
        # self.height = a

    def area(self):
        # print("echo from child")
        # return self.width * self.height
        return super().area()

    def tell_your_geometric_type(self):
        return "Square"

r1 = Rectangle(10, 5)
print(r1.area())
print(r1.tell_your_geometric_type())
print('-'*80)
s1 = Square(10)
print(s1.area())
print(s1.tell_your_geometric_type())