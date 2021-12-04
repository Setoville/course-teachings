closest_vowel = 'aaeeeiiiiooooouuuuuuu'
consonant = 'bcdfghjklmnpqrstvwxyz'

word = input().lower()
new_word = ''
for i in word:
    x = consonant.find(i)
    new_word += i
    if x > -1:
        new_word = new_word + closest_vowel[x] + consonant[x+1]
print(new_word)
