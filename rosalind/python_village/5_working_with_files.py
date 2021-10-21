# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Make sure the file intended to be opened is in the same directory with the working_with_files.py file
# Create an empty file named output.txt to write the output data (in the same directory)

# Use for loop
f = open('rosalind_ini5.txt', 'r')
g = open('output.txt', 'w')

i = 1
for line in f:
    if i % 2 == 0:
        g.write(line)
    i += 1
f.close()
g.close()

# Or
# A more elegant way
# [1::2] means print out the lines starting from line #1, with an incrementation of 2
f = open('rosalind_ini5.txt', 'r')
g = open('output.txt', 'w')
g.write(''.join(f.readlines()[1::2]))
