# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

a = 3
b = 5

# Print directly
print (a ** 2 + b ** 2)

# Or
# Use function
def hypotenuse(a, b):
    return a ** 2 + b ** 2

print (hypotenuse(a, b))
