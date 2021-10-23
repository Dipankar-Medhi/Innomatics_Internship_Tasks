"""
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

No more than  rejects?
At least  rejects?"""

import math as m


def binom_dist(x, n, p):
    combination = (m.factorial(n))/(m.factorial(x)*(m.factorial(n-x)))
    binom = combination*((p/100)**x)*((1-(p/100))**(n-x))
    return binom


prob_rej, n = list(map(float, input().split(" ")))

print(round(sum([binom_dist(i, n, prob_rej) for i in range(0, 3)]), 3))

print(round(sum([binom_dist(i, n, prob_rej) for i in range(2, 11)]), 3))
