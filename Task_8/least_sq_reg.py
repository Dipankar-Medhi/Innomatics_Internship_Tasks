n = 5
xy = [map(int, input().split()) for _ in range(n)]

sum_x, sum_y, sum_x2, sum_xy = map(
    sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))

# Finding the value of b
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

# FInding the mean y bar
y_bar = sum_y/n
# Finding the value of a
a = y_bar - b * (sum_x / n)
print('{:.3f}'.format(a + b * 80))
