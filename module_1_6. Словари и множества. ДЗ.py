my_dict = {'Bob' :1998, 'Jack' : 1999}
print(my_dict)
print(my_dict['Bob'])
print(my_dict.get('Mike'))
print(my_dict)
my_dict['Jim'] = 2000
my_dict['Ron'] = 2001
A = my_dict.pop('Jim')
print(A)
print(my_dict)
set_ = {1, 1, 1, 2, 3, False, (2, 3, 4), 'word'}
print(set_)
set_.add(5)
set_.add(6)
print(set_.discard(5))
print(set_)

