def pow2(n):
    return n ** 2


pow2_new = lambda n: n**2
mysum = lambda a, b: a + b

val = pow2(10)
val_new = pow2_new(10)
sum_val = mysum(10, 20)
print(val)
print(val_new)
print(sum_val)
print(type(pow2))
print(type(pow2_new))