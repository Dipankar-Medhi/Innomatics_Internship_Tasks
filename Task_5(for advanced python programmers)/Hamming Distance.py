"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


print(Solution().hammingDistance(6, 4))
