def solution1(word):
    closest_vowels = 'aaaeeeeiiiiioooooouuuuuuuu'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    result = ""
    for letter in word:
        if letter in vowels:
            result += letter
        else:
            # rule 1
            result += letter
            # rule 2
            alpha_index = alphabet.index(letter)
            result += closest_vowels[alpha_index]
            # rule 3
            if letter == 'z':
                result += 'z'
            else:
                offset = 1
                while alphabet[alpha_index + offset] in vowels:
                    offset += 1
                result += alphabet[alpha_index + offset]
    return result


# something to think about...
def solution2(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowel_indexes = {
        'a': 0,
        'e': 4,
        'i': 8,
        'o': 14,
        'u': 20
    }
    # this assumes letter is NOT a vowel.

    def find_closest_vowel(letter):
        letter_index = alphabet.index(letter)
        closest_vowel_index = 0
        closest_vowel_distance = 25
        for vowel in vowel_indexes:
            if abs(letter_index - vowel_indexes[vowel]) < closest_vowel_distance:
                closest_vowel_distance = abs(
                    letter_index - vowel_indexes[vowel])
                closest_vowel_index = vowel_indexes[vowel]
        return alphabet[closest_vowel_index]

test_words = ['joy', 'ham', 'game']

for w in test_words:
    result = solution1(w)
    print(result)
