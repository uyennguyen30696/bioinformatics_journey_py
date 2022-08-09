# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

# This problem is actually fiding factorial of n and print all possible permutations
# Reference: https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

# Read data from file
dataFile = open('txt_files/19_rosalind_perm.txt', 'r')
n = int(dataFile.read())
dataFile.close()

# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

perms = factorial(n)
print (perms)

# Create a list of integers from 1 to perms
def createList(n):
    perm_arr = [num for num in range(1, n + 1)]
    perm_str = ''
    for num in perm_arr:            # Convert each integer in the array into string
        perm_str += str(num)
    return perm_str
perms_list = list(createList(n))

# Method 1 (use built-in itertools)
# from itertools import permutations
# result = list(permutations(range(1, n + 1)))
# for i in range(len(result)):
#     print (*result[i])

# Method 2 (backtracking)
def permutation(perms_list):
    # If number of permutation is 1, there is only one permutation
    if len(perms_list) == 1:
        return perms_list

    # If perms is > 1
    result = []     # Empty list to store permutations

    for i in range(len(perms_list)):
        # Extract perms[i] from the perms list
        curr = perms_list[i]

        # Remaining list after extraction
        remList = perms_list[:i] + perms_list[i + 1:]

        # Generate all permutations where curr is the first element
        for p in permutation(remList):
            result.append(curr + p)

    return result

g = open('output.txt', 'w')
for p in permutation(perms_list):
    g.write(' '.join(p) + '\n')
    print (' '.join(p))
