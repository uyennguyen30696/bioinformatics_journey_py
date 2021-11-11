# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

f = open('txt_files/13_rosalind_iev.txt', 'r').readline().split()
num_couples = [int(i) for i in f]
result = 2 * (num_couples[0] + num_couples[1] + num_couples[2] + num_couples[3] * 0.75 + num_couples[4] * 0.5)
print (result)
