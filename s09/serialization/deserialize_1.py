f = open('my_stored_list.txt', 'r')
str_a = f.read()
f.close()

a = eval(str_a)