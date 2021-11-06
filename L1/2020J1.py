S = int(input())
M = int(input())
L = int(input())

score = S + (2 * M) + (3 * L)
print(score)
if score >= 10:
    print('happy')
else:
    print('sad')
