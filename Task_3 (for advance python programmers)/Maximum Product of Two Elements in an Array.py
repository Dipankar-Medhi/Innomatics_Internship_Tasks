"""Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:
Input: nums = [3,4,5,2]
Output: 12 """

# Without the built in max function


class Solution:
    def maxProduct(self, nums):
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    result.append((nums[i]-1)*(nums[j]-1))

        return self.findMax(result)

    def findMax(self, nums):
        max_num = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
        return max_num


# with the built in max function


class Solution:
    def maxProduct(self, nums):
        first_max = max(nums)
        nums.remove(first_max)
        second_max = max(nums)
        return (first_max-1)*(second_max-1)


print(Solution().maxProduct([3, 7]))
