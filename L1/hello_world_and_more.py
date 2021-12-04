### BASICS ###
# Two main types of variables
my_name = "andrew"
my_age = 22

# What can we do with these?
# Mathematical operations! Add 1!
my_age_next_year = my_age + 1
#output: 23

# String "word" manipulation
my_name_cool = my_name + "cool"
# output: andrewcool


### INPUT/OUTPUT ###

# user input, they write this into the terminal.
# input a string.
# op1 = input()
# op2 = input()

# input an integer.
B = int(input())

# If you are working with integers, you can perform
# mathematical operations:

# res = op1 + op2
P = (5 * B) - 400
# Remember PEDMAS (or BEDMAS).

# user output, they see this
print(P)

### IF statements ###
# conditional printing.
# we only print if the statement (P == 100) is true.
if P == 100:
    print(0)
elif P > 100:
    print(1)
else:
    print(-1)
