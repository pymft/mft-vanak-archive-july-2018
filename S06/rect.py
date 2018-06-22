class Rectangle:
    name = 'Rectangle'
    
    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        area = self.height * self.width
        return area

    


r1 = Rectangle(10, 20)
r2 = Rectangle(3, 10)
