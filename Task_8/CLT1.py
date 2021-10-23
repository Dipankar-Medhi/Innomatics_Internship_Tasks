"""
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. Check out the Tutorial tab for learning materials!

Task
A large elevator can transport a maximum of  pounds. Suppose a load of cargo containing  boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of  pounds and a standard deviation of  pounds. Based on this information, what is the probability that all  boxes can be safely loaded into the freight elevator and transported?"""

import math

x = 9800
n = 49
mu = 205
sigma = 15

mu_bar = n * mu
sigma_bar = math.sqrt(n) * sigma


def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))


print(round(cdf(x, mu_bar, sigma_bar), 4))
