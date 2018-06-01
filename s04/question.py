inp = [1, 2, 3, 4, 100, 2]
# out = [4800 , 2400 , 1600 , 1200 , 48   , 2400 ]

# order O
A = 1
for val in inp:
    A *= val

def mapfun(x):
    return A/x


print(A)
out = map(lambda x: A/x, inp)
print(list(out))