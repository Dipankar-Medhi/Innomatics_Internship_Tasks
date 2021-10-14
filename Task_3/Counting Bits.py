"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
 

Example 1:
Input: n = 2
Output: [0,1,1]
"""


class Solution:
    def countBits(self, num: int):
        resutl = [0]
        for i in range(1, num+1):
            resutl.append(resutl[i >> 1] + i % 2)
        return resutl


print(Solution().countBits(2))
