# REVIEW of LOOPS

counter = 0
while counter < 10:
    print('hello while')
    counter += 1

for counter in range(10):
    print('hello for')
    # note- we don't need to increment counter when using a for-loop
    # counter += 1

# REVIEW of LISTS


# for cookie in cookie_list:
#     print(cookie)

# length of a list (or a string)
# print(len(cookies))  # prints 3
# print(len(cookies[1]))  # prints 9

# # indexing by 0, incredible!
# print(cookies[1])

# END REIVEW

# tuples
cookie_list = ["oatmeal", "chocolate", "cinnamon"]
# IMMUTABLE. This does NOT change.
cookie_tuple = ("oatmeal", "chocolate", "cinnamon")

cookie_list[2] = "raisin"

# ILLEGAL.
# cookie_tuple[2] = "raisin"

# functions
# we organize our code by putting them into a "box", called a "function"
# once we build this box, we don't really care about what happens INSIDE the box,
# we only care about inputs and outputs to this box.

# why? REUSABILITY.


def add(num1, num2):
    result = num1 + num2
    return result


total = add(5, 7)

total = 5 + 7


# simple string formatting
print("my favourite cookie is %s" % 'oatmeal')
