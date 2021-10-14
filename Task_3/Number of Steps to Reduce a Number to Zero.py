"""Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
 
Example 1:
Input: num = 14
Output: 6"""


class Solution:

    def numberOfSteps(self, num: int) -> int:
        r = 0
        return self.findStep(num, r)

    def findStep(self, num, r):

        while (num > 0):
            if num % 2 == 0:
                return r + 1 and self.findStep(num/2, r+1)
            elif num % 2 != 0:
                return r + 1 and self.findStep(num - 1, r+1)
        return r


print(Solution().numberOfSteps(123))
