import numpy

n, m = map(int, input().split(" "))
arr = numpy.array([input().split(" ") for _ in range(n)], int)

minimum = numpy.min(arr, axis=1)

print(numpy.max(minimum))
