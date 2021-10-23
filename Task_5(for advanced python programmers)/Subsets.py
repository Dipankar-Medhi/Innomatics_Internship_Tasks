"""Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]"""


# class Solution:
#     def subsets(self, nums):
#         result = [[]]

#         for n in nums:
#             for i in range(len(result)):

#                 # Since [] + [1] = [1], [1] + [2] = [1,2], and so on...
#                 result.append(result[i]+[n])
#         return result

class Solution:
    def subsets(self, nums):
        # for example nums is [5, 6, 1], input number is 3, convert to binary is 011, then return list should be [6, 1]
        # if input number is 5 which binary is 101, then return list is [5, 1]
        def bit2list(n):
            ret = []
            idx = 0
            while n:
                if n & 1:
                    ret.append(nums[idx])
                n >>= 1
                idx += 1
            return ret
        # convert nums to binary, if len(nums)=3, output is 111; if len(nums)=4, output is 1111
        base, one = 0, 1
        for _ in range(len(nums)):
            base += one
            one <<= 1
        # Use bit manipulation to find subsets; e.g. base=11, subsets: 10, 01
        ret = []
        mask = base
        while mask:
            ret.append(bit2list(mask))
            mask = (mask - 1) & base
        return ret + [[]]


print(Solution().subsets([1, 2, 5]))
