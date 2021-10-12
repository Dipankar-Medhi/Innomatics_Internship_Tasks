"""Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4"""


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1

        return result


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
