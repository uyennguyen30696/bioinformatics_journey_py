# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Make sure the file intended to be opened is in the same working directory with the 5_working_with_files.py file
# The output.txt file will be created after executing the code

# Use for loop
f = open('txt_files/5_rosalind_ini5.txt', 'r')
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
f = open('txt_files/rosalind_ini5.txt', 'r')
g = open('output.txt', 'w')
g.write(''.join(f.readlines()[1::2]))
