import numpy

n, m = map(int, input().split(" "))

arr = numpy.array([input().split(" ") for _ in range(n)], int)

summation = numpy.sum(arr, axis=0)

print(numpy.prod(summation, axis=None))
