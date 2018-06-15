def function_maker(f):
    def inner_function(*args):
        res = "<i>" + str(f(*args)) + "</i>"
        return res
    return inner_function

@function_maker
def echo_text(s):          # another_function_maker(echo_text)
    return s

@function_maker
def fact(n):
    val = 1
    while n > 0:
        val *= n
        n -= 1
    return val

@function_maker
def my_pow(a, b):
    return a ** b



# echo_text = function_maker(echo_text)

print(echo_text('hello'))
print(fact(10))
print(my_pow(2, 10))

