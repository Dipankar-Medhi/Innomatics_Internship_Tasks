
# true population distribution
mean, std = 500, 80

# sample mean distribution
meanS, sigmaS = mean, std/(100**0.5)

# confidence intervals of sample mean dist
A = mean - (1.96*sigmaS)
B = mean + (1.96*sigmaS)

print(round(A, 2))
print(round(B, 2))
