"""You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results."""

import numpy


nos_nm = input().split(" ")
n, m = int(nos_nm[0]), int(nos_nm[1])
arr = []


for _ in range(n):
    arr.append(numpy.array(input().split(" "), int))


my_arr = numpy.array(arr)
print(numpy.transpose(my_arr))
print(my_arr.flatten())
