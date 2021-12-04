# a <- 3 -> b
# b <- 10 -> c
# c <- 12 -> d
# d <- 5 -> e

# 0 means we're in this city!
# 3 to the next city
# 13 = 3 + 10
# 25 = 13 + 12

# take what number we're "ON", add what's "before it"

# A---B----------C------------D-----E
# A-3-B-----10---C-----12-----D--5--E
# 3 10 12 5
city_distances = input().split()

for i in range(len(city_distances)):
    city_distances[i] = int(city_distances[i])

# print(city_distances)

# position (absolute)
# 0--3---------13-----------25----30

#[3, 10, 12, 5]

# positions list.
# [0,3,13,25,30]
positions = [0] * 5
for i in range(1, len(positions)):
    positions[i] = positions[i-1] + city_distances[i-1]

# print(positions)

# output_list = []
for i in range(5):
    for j in range(5):
        dis = abs(positions[j] - positions[i])
        print(dis, end=" ")
    print("")
# # distance between A and A
# dis = positions[0] - positions[0]  # 0
# # distance between A and B
# dis = positions[1] - positions[0]  # 3
# # distance between A and C
# dis = positions[2] - positions[0]  # 13
# # distacne between A and D
# dis = positions[3] - positions[0]  # 25
# # distacne between A and E
# dis = positions[4] - positions[0]  # 30
