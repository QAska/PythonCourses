vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = []

for letter in word:
    if letter not in found:
        if letter in vowels:
            found.append(letter)

for vowel in found:
    print(vowel)

print(len(found))