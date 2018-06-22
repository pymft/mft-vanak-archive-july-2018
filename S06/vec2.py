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
        # v1, v2 = self, other
        # if v1.dim > v2.dim:
        #     v1, v2 = v2, v1
        #     v11 = [v1.vals[i] if i<= v1.dim else 0 for i in range(v2.dim)]
        if len(self.vals) == len(other.vals):
            inps = [a + b for a, b in zip(self.vals, other.vals)]
            return Vector(*inps)
        
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.vals)

    

v1 = Vector(10, 2)
v2 = Vector(3, 5)




