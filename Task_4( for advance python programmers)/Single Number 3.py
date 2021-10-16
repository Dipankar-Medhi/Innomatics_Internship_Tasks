"""Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]"""


class Solution:
    def singleNumber(self, nums):
        i = 0
        return self.findNum(nums, i)

    def findNum(self, arr, i):
        result = []
        temparr = []
        while(i < len(arr)):
            element = arr.pop(i)
            if element in temparr or element in arr:
                temparr.append(element) and self.findNum(arr, i)
        # elif element in temparr and element not in arr:
        #     self.findNum(arr, i+1)
            elif element not in temparr and element not in arr:
                result.append(element) and self.findNum(arr, i)

        return result


print(Solution().singleNumber([0, 1, 3, 4, 1, 3, 3]))
