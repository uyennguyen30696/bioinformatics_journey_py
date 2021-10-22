# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

str = 'We tried list and we tried dicts also we tried Zen'
str = str.split()
dict = {}

# Count frequencies of each word in str
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# First way
for word in str:
    dict[word] = str.count(word)

# Second way
for word in str:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Return key, value
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# First way, Loop through dict
for key in dict:
    print (key, dict[key])

# Or
# Second way, use .items() to return key, value pairs
for key, value in dict.items():
    print (key, value)
