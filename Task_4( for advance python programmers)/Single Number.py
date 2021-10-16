"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:
Input: nums = [2,2,1]
Output: 1"""


class Solution:
    def singleNumber(self, nums) -> int:
        nums2 = list(set(nums))
        sum_num2 = sum(nums2)
        sum_num1 = sum(nums)
        return sum_num2*2 - sum_num1


print(Solution().singleNumber([4, 1, 2, 1, 2]))
