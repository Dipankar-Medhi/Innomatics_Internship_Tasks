import numpy

num_shape = tuple(map(int, input().split()))
print(numpy.zeros(num_shape, dtype=numpy.int))
print(numpy.ones(num_shape, dtype=numpy.int))
