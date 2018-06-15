# decorator

var = 10

def echo(x, y):
    # shadowing
    var = 1
    print(locals())
    print(globals())
    return x


echo(1, 2)
print(echo)
