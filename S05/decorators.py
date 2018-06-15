def function_maker(f):
    def inner_function(arg):
        res = "<i>" + f(arg) + "</i>"
        return res
    return inner_function

def another_function_maker(f):
    def inner_function(arg):
        res = "<b>" + f(arg) + "</b>"
        return res
    return inner_function

# DECORATOR PATTERN
@function_maker            # function_maker(another_function_maker(echo_text))
@another_function_maker    # <-----------echo_text---------->
def echo_text(s):          # another_function_maker(echo_text)
    return s

# echo_text = function_maker(echo_text)

print(echo_text('hello'))

