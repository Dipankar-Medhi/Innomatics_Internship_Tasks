import numpy

a = int(input())

arr_1 = numpy.array([input().split() for _ in range(a)], int)
arr_2 = numpy.array([input().split() for _ in range(a)], int)

print(numpy.dot(arr_1, arr_2))
