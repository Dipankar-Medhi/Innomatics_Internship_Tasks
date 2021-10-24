"""Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]"""


class Solution:
    def subsets(self, nums):
        result = [[]]

        for n in nums:
            for i in range(len(result)):

                # Since [] + [1] = [1], [1] + [2] = [1,2], and so on...
                result.append(result[i]+[n])
        return result


print(Solution().subsets([1, 2, 5]))
