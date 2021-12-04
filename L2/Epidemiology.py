P = int(input())
# number of people initially with infection
N = int(input())
R = int(input())

# P = 750
# N = 1
# R = 5

# day = 0, N = 1
# day = 1, total = 5 + 1 = 6
# day = 2, total = 5*5 + 5 + 1 = 31
# day = 3, total = 25*5 + (5*5) + 5 + 1 = 156
# day = 4, total = 125*5 + 25*5 + 5*5 + 5 + 1 = 781

# 1 + 5 + 25 + 125 + 625
# 5**0, 5**1, 5**2, 5**3, 5**4


day = 1
total_people_infected = N
# day = 1
# total_ppl_inf = 1
while day < 5:
    newly_infected = R ** day
    # newly_infected = 5 ** 1
    total_people_infected = total_people_infected + newly_infected
    day += 1
print(total_people_infected)
# HOMEWORK
# In this code, there exists a case in the problem that is unaccounted for.
# Run with this input: 10 2 1

# HOMEWORK 2
# Complete the homework based on question specs.
# total_people_infected is not the right output!!
# print the right value.
