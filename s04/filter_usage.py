lst = [1, 2, 3, 4, 5, 6, 7, 8]

out2 = [x ** 2 for x in lst if x % 2 == 0]

out = []
for x in lst:
    if x % 2 == 0:
        out.append(x**2)

out3 = filter(lambda x: x % 2 == 0, lst)

print(out)
print(out2)
print(list(out3))