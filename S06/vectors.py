class Vector:
    description = 'vector'

    def __init__(self, *inps):
        self.vals = inps  # (10, 2)

    @property
    def dim(self):
        return len(self.vals)
    
    @property
    def length(self):
        len_pow2 = sum([x ** 2 for x in self.vals]) 
        length = len_pow2 ** 0.5
        return  length

    def __add__(self, other):
        # zip(self.vals, other.vals)
        if len(self.vals) == len(other.vals):
            inps = [a + b for a, b in zip(self.vals, other.vals)]
            return Vector(*inps)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            # dot product
            return Vector(self.x * other.x, self.y * other.x)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "[%s %s]" % (self.x, self.y)

    

v1 = Vector(10, 2)
v2 = Vector(3, 5)
v3 = v1.multiply_by_scalar(2)
# v4 = v1.add(v2)
print(v1.length)
print(v3.length)


