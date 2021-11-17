# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# Problem interpretation
# If m = 3 (rabbits die after 3 months)
# The young pairs need one month to grow up first, then reproduce the month after
# Month 1: 1 pair (young)
# Month 2: 1 pair (adult)
# Month 3: 1 pair (adult) + 1 pairs (young) = 1 + 1 total
# Month 4: 1 + 1 pairs (adult) + 1 pairs (young) = 2 + 1 total - 1 pair adult
# Month 5: 2 pairs (adult) + 1 pairs (young) = 2 + 1 total 
# Month 6: 3 pairs (adult) + 2 pairs (young) = 3 + 2 total - 1 pair adult
# ...

# f(0) = 1
# f(1) = 1
# f(n, m) = f(n - 1) + f(n - 2) - f(n - (m + 1))

n = 83 
m = 19

def mortalFib(n, m):
    f = [1, 1, 1]
    for i in range(3, n + 1):
        f.append(f[i - 1] + f[i - 2])
        if (i > m):
            f[i] -= f[i - (m + 1)]
    return f[n]
print (mortalFib(n, m))
