import json

f = open('pickled_data.json', 'r')
data_new = json.load(f)
# locals().update(data_new)
print (data_new)