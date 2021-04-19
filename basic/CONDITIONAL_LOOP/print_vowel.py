vowels = set('aeiou')
word = input('Enter a word to test: ')

found = vowels.intersection(set(word))

for vowels in found:
    print(vowels)
