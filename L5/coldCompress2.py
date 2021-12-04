# aaabbbcc

# 3 a 3 b 2 c
N = int(input())
words = []
output = []
for i in range(N):
    words.append(input())

# output = [[#times_occured, letter_seen],]
for i in range(N):
    output.append([])
    for j in range(len(words[i])):
        if j == 0:
            output[i].append([1, words[i][j]])
        else:
            # track if the letter before this letter
            # was the same letter as we have now.
            if words[i][j] == output[i][-1][1]:
                output[i][-1][0] += 1
            else:
                output[i].append([1, words[i][j]])

print(output)
for line in output:
    for letter in line:
        print(letter[0], end=' ')
        print(letter[1], end=' ')
    print('')




    
