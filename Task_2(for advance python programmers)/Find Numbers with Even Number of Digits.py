"""Given an array nums of integers, return how many of them contain an even number of digits.
 
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2"""


class Solution:
    def findNumbers(self, nums) -> int:
        result = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                result += 1

        return result


print(Solution().findNumbers([12, 345, 2, 6, 7896]))
