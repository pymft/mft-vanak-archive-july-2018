def add_newline(f):
    def inner(self, val):
        return f(self, val + '\n')
    return inner

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("I'm here")

    def openfile(self, filename):
        self.f = open(filename, 'a')

    @add_newline
    def write(self, val):
        self.f.write(val)

    def closefile(self):
        self.f.close()


s1 = Singleton()
s1.openfile('./sample.txt')
s1.write('hello from s1')
s2 = Singleton()
s2.write('hello from s2')
s2.closefile()
print(id(s1), id(s2))
print(s1 is s2)
print(s1)