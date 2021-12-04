# the 0 is assumed. you don't need to include it.
# for i in range(0, 5):


# dictionary, maps. Same thing functionally
cheese_dct = {}

# cheese: strength
# cheddar: 5
# gouda: 3
# blue: 10
# enter items in our dct
cheese_dct['cheddar'] = 5
cheese_dct['gouda'] = 3
cheese_dct['blue'] = 10

print(cheese_dct)
# access "lookup" item in dct
print(cheese_dct['blue'])

# update item in dct. this looks the same as entering items originally.
cheese_dct['blue'] = "awesome"

print(cheese_dct['blue'])
#['a', 1]

# list
cheese_list = ['cheddar', 'gouda', 'blue', 'american', 'parmesian']

print(cheese_list[1])

# append
cheese_list.append("swiss")
print(cheese_list)

# insert. beware @@this changes ALL of your indices
cheese_list.insert(5, "mozza")
print(cheese_list)

# queue. FIFO first in first out.
next_element = cheese_list.pop(0)
print(next_element)
# pop(0) removes first element from the list.
next_element = cheese_list.pop(0)
print(next_element)

# cheese_list.remove('gouda')
# print(cheese_list)
# cheese_list.pop(2)
# print(cheese_list)

# stack. LIFO. last in first out.
cheese_plates = ['cheddar', 'gouda', 'blue', 'american', 'parmesian']

cheese_plates.append('swiss')
highest_element = cheese_plates.pop()
print(highest_element)
