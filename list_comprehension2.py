#List of cubes from 1 to 10
cubes = [i*i*i for i in range(1,11)]
print(cubes)

#Extract all vowels from a string
string = "My name is Alice"
vowels = "aeiouAEIOU"

vowels_string = [c for c in string if c in vowels]
print(vowels_string)

# Convert every word in a sentence to uppercase
sentence = "Python"
sentence = [c.upper() for c in sentence]
print(sentence)