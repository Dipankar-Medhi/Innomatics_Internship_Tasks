""" Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]."""


class Solution:
    def runningSum(self, nums):

        # initializing sum variable.
        sum = 0

        # initializing result array for output.
        result = []

        # iterating through the given array and adding sum to the ith element.
        for i in range(len(nums)):
            sum = sum + nums[i]
            result.append(sum)

        return result


print(Solution().runningSum([3, 1, 2, 10, 1]))
