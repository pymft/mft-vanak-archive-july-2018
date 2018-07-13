a = [1, 2, 3]

str_a = str(a)

f = open('my_stored_list.txt', 'w')
f.write(str_a)
f.close()

print (a)