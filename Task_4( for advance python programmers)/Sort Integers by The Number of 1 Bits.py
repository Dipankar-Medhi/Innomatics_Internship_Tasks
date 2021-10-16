"""Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.

 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]"""


class Solution:
    def sortByBits(self, arr):

        # bin(x)[2:] removes the first 2 characters 0b
        sorted_arr = sorted(arr, key=lambda x: (bin(x)[2:].count("1"), x))
        return sorted_arr


print(Solution().sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
