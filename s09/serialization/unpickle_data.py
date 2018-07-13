import pickle

f = open('pickled_data.p', 'rb')
data_new = pickle.load(f)
# locals().update(data_new)
print (data_new)