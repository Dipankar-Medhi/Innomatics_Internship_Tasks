"""
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).
"""


import math as m


def binom_dist(x, n, p):
    combination = (m.factorial(n))/(m.factorial(x)*(m.factorial(n-x)))
    binom = combination*(p**x)*((1-p)**(n-x))
    return binom


boys, girls = list(map(float, input().split(" ")))
odds = boys / girls

results = []
for i in range(3, 7):
    results.append(binom_dist(i, 6, odds / (1 + odds)))

print(round(sum(results), 3))
