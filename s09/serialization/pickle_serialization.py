import pickle
# import cPickle as pickle

my_data =  {'value': 1, 'value_float':1.23, 'bool_data':True}
f = open('pickled_data.p', 'wb')

pickle.dump(my_data, f)