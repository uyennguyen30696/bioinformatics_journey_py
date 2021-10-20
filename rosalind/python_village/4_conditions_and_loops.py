# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Use for loop
a = 4449 
b = 9155
sum = 0
for i in range(a, b+1):
    if (i % 2) == 1:
        sum += i
print (sum)

# Or
# Use bitwise-Or
# Convert numbers to binaries. Odd numbers always finish with 1 and even numbers always finish with 0. So a|1 means starting value is an odd number
# 2 means incrementation of 2 (like i += 2)
print (sum(range(a|1, b+1, 2)))
