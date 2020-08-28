# Lists support + and * operators
my_list = []
my_list.append('a')

my_list_2 = my_list + ['b', 'c', 'd']
print(my_list_2)

my_list_3 = my_list_2 * 2
print(my_list_3)

my_list_4 = [1, 2, 3] * 3
print(my_list_4)

# They also support slices notation
my_list_5 = [1, 2, 'a', 'b']
print(my_list_5)
print(my_list_5[::-1])
print(my_list_5[1:])
print(my_list_5[1:5:2])

# Lists are muttable
names = ['Juan', 'Pedro', 'Enrique']
names[0] = 'Jorge'
print(names)

names.append('Mario')
print(names)

name = names.pop() # Extract the last element
print(names)
print(name == 'Mario')

names.sort()
print(names)

names.extend([20, 22, 21]) # Instead of + operator
print(names)

del names[0] # Delete certain element
del names[2]
print(names)

# Convert string to list
foo = 'foo'
bar = list(foo)
del bar[2]
qux = ''.join(bar)
print(type(qux))
print(qux)
