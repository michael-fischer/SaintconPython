# the hard way
text = 'supercalifragilisticexpialidocious'
count = {}  # Creates an empty dictionary

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
# will print
#     {'s': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'c': 3, 'a': 3, 'l': 3, 'i': 7, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1, 'o': 2}

# now let's explore removing items from this dictionary.
# how would we remove the vowels

vowels = 'aeiou'
for vowel in vowels:
    del count[vowel]
    
print(count)
# will print
#     {'c': 3, 'd': 1, 'g': 1, 'f': 1, 'l': 3, 'p': 2, 's': 3, 'r': 2, 't': 1, 'x': 1}