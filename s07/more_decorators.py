def tag_maker(tag):
    def decorator(f):
        def inner_function(*args):
            # res = "<{tag}>{result}</{tag}>".format(tag=tag, result=str(f(*args)) )
            res = "<" + tag+ ">" + str(f(*args)) + "</" + tag + ">"
            return res
        return inner_function
    return decorator


@tag_maker('span')
@tag_maker('i')
def echo(s):
    return s

print(echo('Helllllllo'))