import json

num = 1

my_data =  {'value': 1, 'value_float':1.23, 'bool_data':True}
f = open('pickled_data.json', 'w')

json.dump(my_data, f)