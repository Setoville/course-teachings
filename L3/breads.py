bread_name = "sourdough"

# Appending. Concat.
full_bread_name = "awesome " + bread_name + " bread"
print(full_bread_name)

# # breaking up a string!
# for character in "awesome sourdough bread":
#     print(character)

# THIS IS SUPER IMPORTANT. More on this later.
bread_list = ['sourdough', 'wholewheat', 'white']
for bread in bread_list:
    print(bread)

cool_word = "cool"
print(cool_word * 3)
# coolcoolcool

# .replace() can be used to substitute a substring
# and to straight up remove a string from another string
final_word = "supercool".replace("cool", "")
print(final_word)

cool_username = "xx_andrew_xx"

# .strip() to remove characters matching from the front and back
# of a string
less_cool_username = cool_username.strip("x_")
print(less_cool_username)

# convert list to single string
bread_string = "--".join(bread_list)
print(bread_string)

# determine length of string
print(len("apple"))  # 5

# THIS IS SUPER IMPORTANT. More on this later.
bread_list = ['sourdough', 'wholewheat', 'white']
bread_costs = [1, 3, 5]
total_cost = 0
for cost in bread_costs:
    total_cost += cost

# modulus operator. new math operation!
print(10 % 3)

# string "slices"
alphabet = 'abcdefg'
# index from 0
print(alphabet[2:8])  # => "c"

# RANGE
bread_length = len(bread_list)
for i in range(bread_length):
    print(i, bread_list[i])
