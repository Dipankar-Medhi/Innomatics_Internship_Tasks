"""Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.

Sample Input

1 2 3 4 -8 -10
Sample Output

[-10.  -8.   4.   3.   2.   1.]"""

import numpy


def arrays(arr):
    for i in range(len(arr)):
        arr[i] = float(arr[i])
    return numpy.array(arr)[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
