def name_of_function(arg1, arg2, kwarg1=10):
    return arg1, arg2, kwarg1


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

val = name_of_function(1, 2, kwarg1=100)
print(val)
print(type(val))

print("10! = ", fact(10))