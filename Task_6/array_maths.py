import numpy


n, m = map(int, input().split(" "))

a = numpy.array([input().split(" ") for _ in range(n)], int)
b = numpy.array([input().split(" ") for _ in range(n)], int)

print(a+b)
print(a-b)
print(a*b)
print(numpy.array(a/b, dtype=int))
print(a % b)
print(a**b)
