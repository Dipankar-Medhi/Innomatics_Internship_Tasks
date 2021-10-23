"""
Objective
In this challenge, we learn about normal distributions. Check out the Tutorial tab for learning materials!

Task
In a certain plant, the time taken to assemble a car is a random variable, , having a normal distribution with a mean of  hours and a standard deviation of  hours. What is the probability that a car can be assembled at this plant in:

Less than  hours?
Between  and  hours?"""

import math
mean, std = 20, 2


def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round(cdf(19.5), 3))
print(round((cdf(22)-cdf(20)), 3))
