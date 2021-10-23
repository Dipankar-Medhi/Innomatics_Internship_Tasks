import numpy

arr = numpy.array([input().split() for _ in range(int(input()))], float)

print(round(numpy.linalg.det(arr), 2))
