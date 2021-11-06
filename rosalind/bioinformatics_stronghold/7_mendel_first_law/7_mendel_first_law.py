# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

# Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree.

# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Problem break down, see my photo note attached in this folder for more details
# The problem actually has 2 different parts:
# 1. Probability of 2 organisma mate 
# 2. Probability of offspring has dominant allele (AA or Aa from Punnett square)

k = 2
m = 2
n = 2

# Population = total
pop = k + m + n

# Probability of the first k wil mate
pk1 = k / pop

# Probability of the first m wil mate
pm1 = m / pop

# Probability of the first n will mate
pn1 = n / pop

# Probability of the second organism will mate with the first organism 
# k x k, k x m, k x n
kk = (k - 1) / (pop - 1)
km = m / (pop - 1)
kn = n / (pop - 1)

# m x k, m x m, m x n
mk = k / (pop - 1)
mm = (m - 1) / (pop - 1)
mn = n / (pop - 1)

# n x k, n x m, n x n
nk = k / (pop - 1)
nm = m / (pop - 1)
nn = (n - 1) / (pop - 1)

# Probability of offspring has dominant allele
kkD = pk1 * kk * 1
kmD = pk1 * km * 1
knD = pk1 * kn * 1

mkD = pm1 * mk * 1
mmD = pm1 * mm * 0.75
mnD = pm1 * mn * 0.5

nkD = pn1 * nk * 1
nmD = pn1 * nm * 0.5
nnD = pn1 * nn * 0

result = round(kkD + kmD + knD + mkD + mmD + mnD + nkD + nmD + nnD, 5)

print (result)
