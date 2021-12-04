num_lines = int(input())

#letter_count = 1
#word         aaaaaaabbbbbcc
#letter_index       ^
#
# 3a 2b 2c

for line in range(num_lines):
    word = input()
    letter_index = 0
    while letter_index < len(word):
        current_letter = word[letter_index]
        letter_count = 1
        letter_index += 1
        while letter_index < len(word) and word[letter_index] == current_letter:
            letter_count += 1
            letter_index += 1
        print(letter_count, current_letter, end=' ')
    print()
