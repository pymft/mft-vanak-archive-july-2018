lst = [1, 2, 3, 4, 5]
out = map(str, lst)
out2 = [str(x) for x in lst]
print(list(out))
print(out2)

fun = lambda x: x ** 2
lst_pow2 = [fun(x) for x in lst]
print(lst_pow2)