class Square:
    def __init__(self, a):
        print(self.__class__.__bases__)
        self.a = a
        self.__area = self.a ** 2

    @property
    def area(self):
        return self.__area

    @area.setter
    def area (self, value ):
        self.__area = value
        self.a = self.__area ** 0.5

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        print("get attribute ", item)
        return super().__getattribute__(item)


s1 = Square(10)
# print(s1.a)
# s1.area = 81
#print(s1.a)
# s1.whatever
s1.new_property = 100
print(s1.new_property)
# print(s1.new_property)